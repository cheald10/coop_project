from django.shortcuts import redirect
from django.urls import resolve
from django.http import HttpResponseForbidden
from .models import Division


class COOPPermissionMiddleware:
    """
    Enforces COOP permissions globally:
    - Admins: full access
    - Coordinators: can edit only their division
    - Leadership: read-only
    """

    EDIT_KEYWORDS = ["create", "edit", "update", "delete"]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        user = request.user

        # Allow anonymous users to be handled by login_required decorators
        if not user.is_authenticated:
            return None

        # Admins always allowed
        if user.is_superuser or user.groups.filter(name="COOP Admins").exists():
            return None

        # Determine if this is an edit operation
        path_name = resolve(request.path_info).url_name or ""
        is_edit_operation = any(key in path_name for key in self.EDIT_KEYWORDS)

        # If not an edit operation, allow
        if not is_edit_operation:
            return None

        # Leadership is read-only
        if user.groups.filter(name="Leadership").exists():
            return HttpResponseForbidden("Leadership users cannot modify COOP data.")

        # Coordinators: must match division
        if user.groups.filter(name="Coordinators").exists():
            division = self._get_division_from_kwargs(view_kwargs)
            if division and division.coordinator == user:
                return None
            return HttpResponseForbidden("You are not allowed to edit this division.")

        # Default: deny
        return HttpResponseForbidden("You do not have permission to perform this action.")

    def _get_division_from_kwargs(self, kwargs):
        """
        Extracts a Division instance from URL kwargs.
        Supports both division_id and pk patterns.
        """
        division_id = kwargs.get("division_id") or kwargs.get("pk")
        if division_id:
            try:
                return Division.objects.get(pk=division_id)
            except Division.DoesNotExist:
                return None
        return None
