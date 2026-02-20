import requests
from typing import List, Dict, Any
from django.conf import settings
from core.models import Division, CriticalApplication


class ServiceNowClient:
    """Simple ServiceNow CMDB client for pulling application data."""

    def __init__(self):
        self.instance_url = settings.SNOW_INSTANCE_URL.rstrip("/")
        self.username = settings.SNOW_USERNAME
        self.password = settings.SNOW_PASSWORD
        self.table = getattr(settings, "SNOW_APP_TABLE", "cmdb_ci_service")

    def _headers(self) -> Dict[str, str]:
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def _base_url(self) -> str:
        return f"{self.instance_url}/api/now/table/{self.table}"

    def fetch_applications(self, query: str | None = None, limit: int = 200) -> List[Dict[str, Any]]:
        params = {"sysparm_limit": str(limit)}
        if query:
            params["sysparm_query"] = query
        response = requests.get(
            self._base_url(),
            headers=self._headers(),
            auth=(self.username, self.password),
            params=params,
            timeout=30,
        )
        response.raise_for_status()
        return response.json().get("result", [])


def sync_critical_applications_from_servicenow(division: Division, query: str | None = None) -> dict:
    """
    Pulls applications from ServiceNow and upserts them into CriticalApplication
    for the given division.
    """
    client = ServiceNowClient()
    records = client.fetch_applications(query=query)

    created = updated = 0

    for rec in records:
        name = rec.get("name") or rec.get("u_application_name")
        if not name:
            continue

        defaults = {
            "description": rec.get("description", ""),
            "hosting_environment": rec.get("u_hosting_environment", ""),
            "recovery_tier": rec.get("u_recovery_tier", ""),
            "rto": rec.get("u_rto", ""),
            "vendor_contact": rec.get("u_vendor_contact", ""),
            "dependencies": rec.get("u_dependencies", ""),
            "workarounds": rec.get("u_workarounds", ""),
        }

        _, created_flag = CriticalApplication.objects.update_or_create(
            division=division,
            name=name,
            defaults=defaults,
        )

        if created_flag:
            created += 1
        else:
            updated += 1

    return {"created": created, "updated": updated, "total": len(records)}
