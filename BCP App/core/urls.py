from django.urls import path
from . import views

urlpatterns = [

    # -------------------------
    # Division Management
    # -------------------------
    path("divisions/", views.division_list, name="division_list"),
    path("divisions/<int:pk>/", views.division_detail, name="division_detail"),

    # -------------------------
    # Essential Functions
    # -------------------------
    path(
        "divisions/<int:division_id>/essential-functions/",
        views.essential_function_list,
        name="essential_function_list"
    ),
    path(
        "divisions/<int:division_id>/essential-functions/new/",
        views.essential_function_create,
        name="essential_function_create"
    ),
    path(
        "essential-functions/<int:pk>/edit/",
        views.essential_function_edit,
        name="essential_function_edit"
    ),

    # -------------------------
    # Critical Applications
    # -------------------------
    path(
        "divisions/<int:division_id>/critical-applications/",
        views.critical_application_list,
        name="critical_application_list"
    ),
    path(
        "divisions/<int:division_id>/critical-applications/new/",
        views.critical_application_create,
        name="critical_application_create"
    ),
    path(
        "critical-applications/<int:pk>/edit/",
        views.critical_application_edit,
        name="critical_application_edit"
    ),

    # -------------------------
    # Key Personnel
    # -------------------------
    path(
        "divisions/<int:division_id>/key-personnel/",
        views.key_personnel_list,
        name="key_personnel_list"
    ),
    path(
        "divisions/<int:division_id>/key-personnel/new/",
        views.key_personnel_create,
        name="key_personnel_create"
    ),
    path(
        "key-personnel/<int:pk>/edit/",
        views.key_personnel_edit,
        name="key_personnel_edit"
    ),

    # -------------------------
    # Vital Records
    # -------------------------
    path(
        "divisions/<int:division_id>/vital-records/",
        views.vital_record_list,
        name="vital_record_list"
    ),
    path(
        "divisions/<int:division_id>/vital-records/new/",
        views.vital_record_create,
        name="vital_record_create"
    ),
    path(
        "vital-records/<int:pk>/edit/",
        views.vital_record_edit,
        name="vital_record_edit"
    ),

    # -------------------------
    # Dependencies
    # -------------------------
    path(
        "divisions/<int:division_id>/dependencies/",
        views.dependency_list,
        name="dependency_list"
    ),
    path(
        "divisions/<int:division_id>/dependencies/new/",
        views.dependency_create,
        name="dependency_create"
    ),
    path(
        "dependencies/<int:pk>/edit/",
        views.dependency_edit,
        name="dependency_edit"
    ),

    # -------------------------
    # Alternate Facilities
    # -------------------------
    path(
        "divisions/<int:division_id>/alternate-facilities/",
        views.alternate_facility_list,
        name="alternate_facility_list"
    ),
    path(
        "divisions/<int:division_id>/alternate-facilities/new/",
        views.alternate_facility_create,
        name="alternate_facility_create"
    ),
    path(
        "alternate-facilities/<int:pk>/edit/",
        views.alternate_facility_edit,
        name="alternate_facility_edit"
    ),

    # -------------------------
    # Communications
    # -------------------------
    path(
        "divisions/<int:division_id>/communications/",
        views.communication_list,
        name="communication_list"
    ),
    path(
        "divisions/<int:division_id>/communications/new/",
        views.communication_create,
        name="communication_create"
    ),
    path(
        "communications/<int:pk>/edit/",
        views.communication_edit,
        name="communication_edit"
    ),

    # -------------------------
    # Recovery Priorities
    # -------------------------
    path(
        "divisions/<int:division_id>/recovery-priorities/",
        views.recovery_priority_list,
        name="recovery_priority_list"
    ),
    path(
        "divisions/<int:division_id>/recovery-priorities/new/",
        views.recovery_priority_create,
        name="recovery_priority_create"
    ),
    path(
        "recovery-priorities/<int:pk>/edit/",
        views.recovery_priority_edit,
        name="recovery_priority_edit"
    ),

    # -------------------------
    # Division Metadata (Profile)
    # -------------------------
    path(
        "divisions/<int:division_id>/metadata/",
        views.division_metadata_detail,
        name="division_metadata_detail"
    ),
    path(
        "divisions/<int:division_id>/metadata/edit/",
        views.division_metadata_edit,
        name="division_metadata_edit"
    ),

    # -------------------------
    # COOP Plan Generation + History
    # -------------------------
    path(
        "divisions/<int:division_id>/plan/generate/",
        views.generate_coop_plan_view,
        name="generate_coop_plan"
    ),
    path(
        "divisions/<int:division_id>/plan/history/",
        views.coop_plan_history,
        name="coop_plan_history"
    ),

    # -------------------------
    # Leadership Dashboard
    # -------------------------
    path("dashboard/leadership/", views.leadership_dashboard, name="leadership_dashboard"),

    from . import views

urlpatterns += [
    path(
        "divisions/<int:division_id>/critical-applications/sync-servicenow/",
        views.sync_critical_applications_servicenow,
        name="sync_critical_applications_servicenow",
    ),
]

]
