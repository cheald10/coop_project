from django.core.management.base import BaseCommand
from app.models import Division, ServiceNowIntegrationConfig
from app.integrations.servicenow import sync_critical_applications_from_servicenow


class Command(BaseCommand):
    help = "Sync Critical Applications from ServiceNow for all enabled divisions"

    def handle(self, *args, **options):
        configs = ServiceNowIntegrationConfig.objects.filter(enabled=True)

        if not configs.exists():
            self.stdout.write(self.style.WARNING("No enabled ServiceNow integration configs found."))
            return

        for config in configs:
            division = config.division
            self.stdout.write(f"Syncing ServiceNow apps for division: {division.name}")

            summary = sync_critical_applications_from_servicenow(
                division,
                query=config.query or None,
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f"Division {division.name}: "
                    f"{summary['created']} created, "
                    f"{summary['updated']} updated "
                    f"(total {summary['total']})."
                )
            )
