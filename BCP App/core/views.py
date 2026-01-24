from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Division, EssentialFunction, CriticalApplication, KeyPersonnel,
    VitalRecord, Dependency, AlternateFacility, Communication,
    RecoveryPriority, DivisionMetadata, GeneratedPlan
)
from .forms import (
    EssentialFunctionForm, CriticalApplicationForm, KeyPersonnelForm,
    VitalRecordForm, DependencyForm, AlternateFacilityForm,
    CommunicationForm, RecoveryPriorityForm, DivisionMetadataForm
)
from .services.coop_plan import generate_coop_plan_for_division


# ---------------------------------------------------------
# PERMISSION CHECK
# ---------------------------------------------------------

def can_edit_division(user, division):
    """Admins can edit everything. Coordinators can edit their division only."""
    if not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    if user.groups.filter(name="COOP Admins").exists():
        return True
    if user.groups.filter(name="Coordinators").exists() and division.coordinator == user:
        return True
    return False


# ---------------------------------------------------------
# DIVISION VIEWS
# ---------------------------------------------------------

@login_required
def division_list(request):
    divisions = Division.objects.all()
    return render(request, "divisions/list.html", {"divisions": divisions})


@login_required
def division_detail(request, pk):
    division = get_object_or_404(Division, pk=pk)
    return render(request, "divisions/detail.html", {"division": division})


# ---------------------------------------------------------
# ESSENTIAL FUNCTIONS
# ---------------------------------------------------------

@login_required
def essential_function_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = EssentialFunction.objects.filter(division=division)
    return render(request, "essential_functions/list.html", {"division": division, "items": items})


@login_required
def essential_function_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)

    if not can_edit_division(request.user, division):
        return redirect("essential_function_list", division_id=division.id)

    if request.method == "POST":
        form = EssentialFunctionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.division = division
            obj.save()
            return redirect("essential_function_list", division_id=division.id)
    else:
        form = EssentialFunctionForm()

    return render(request, "essential_functions/form.html", {"form": form, "division": division})


@login_required
def essential_function_edit(request, pk):
    item = get_object_or_404(EssentialFunction, pk=pk)
    division = item.division

    if not can_edit_division(request.user, division):
        return redirect("essential_function_list", division_id=division.id)

    if request.method == "POST":
        form = EssentialFunctionForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("essential_function_list", division_id=division.id)
    else:
        form = EssentialFunctionForm(instance=item)

    return render(request, "essential_functions/form.html", {"form": form, "division": division})


# ---------------------------------------------------------
# CRITICAL APPLICATIONS
# ---------------------------------------------------------

@login_required
def critical_application_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = CriticalApplication.objects.filter(division=division)
    return render(request, "critical_applications/list.html", {"division": division, "items": items})


@login_required
def critical_application_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)

    if not can_edit_division(request.user, division):
        return redirect("critical_application_list", division_id=division.id)

    if request.method == "POST":
        form = CriticalApplicationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.division = division
            obj.save()
            return redirect("critical_application_list", division_id=division.id)
    else:
        form = CriticalApplicationForm()

    return render(request, "critical_applications/form.html", {"form": form, "division": division})


@login_required
def critical_application_edit(request, pk):
    item = get_object_or_404(CriticalApplication, pk=pk)
    division = item.division

    if not can_edit_division(request.user, division):
        return redirect("critical_application_list", division_id=division.id)

    if request.method == "POST":
        form = CriticalApplicationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("critical_application_list", division_id=division.id)
    else:
        form = CriticalApplicationForm(instance=item)

    return render(request, "critical_applications/form.html", {"form": form, "division": division})


# ---------------------------------------------------------
# KEY PERSONNEL
# ---------------------------------------------------------

@login_required
def key_personnel_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = KeyPersonnel.objects.filter(division=division)
    return render(request, "key_personnel/list.html", {"division": division, "items": items})


@login_required
def key_personnel_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)

    if not can_edit_division(request.user, division):
        return redirect("key_personnel_list", division_id=division.id)

    if request.method == "POST":
        form = KeyPersonnelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.division = division
            obj.save()
            return redirect("key_personnel_list", division_id=division.id)
    else:
        form = KeyPersonnelForm()

    return render(request, "key_personnel/form.html", {"form": form, "division": division})


@login_required
def key_personnel_edit(request, pk):
    item = get_object_or_404(KeyPersonnel, pk=pk)
    division = item.division

    if not can_edit_division(request.user, division):
        return redirect("key_personnel_list", division_id=division.id)

    if request.method == "POST":
        form = KeyPersonnelForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("key_personnel_list", division_id=division.id)
    else:
        form = KeyPersonnelForm(instance=item)

    return render(request, "key_personnel/form.html", {"form": form, "division": division})


# ---------------------------------------------------------
# VITAL RECORDS
# ---------------------------------------------------------

@login_required
def vital_record_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = VitalRecord.objects.filter(division=division)
    return render(request, "vital_records/list.html", {"division": division, "items": items})


@login_required
def vital_record_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)

    if not can_edit_division(request.user, division):
        return redirect("vital_record_list", division_id=division.id)

    if request.method == "POST":
        form = VitalRecordForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.division = division
            obj.save()
            return redirect("vital_record_list", division_id=division.id)
    else:
        form = VitalRecordForm()

    return render(request, "vital_records/form.html", {"form": form, "division": division})


@login_required
def vital_record_edit(request, pk):
    item = get_object_or_404(VitalRecord, pk=pk)
    division = item.division

    if not can_edit_division(request.user, division):
        return redirect("vital_record_list", division_id=division.id)

    if request.method == "POST":
        form = VitalRecordForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("vital_record_list", division_id=division.id)
    else:
        form = VitalRecordForm(instance=item)

    return render(request, "vital_records/form.html", {"form": form, "division": division})


# ---------------------------------------------------------
# DEPENDENCIES
# ---------------------------------------------------------

@login_required
def dependency_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = Dependency.objects.filter(division=division)
    return render(request, "dependencies/list.html", {"division": division, "items": items})


@login_required
def dependency_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)

    if not can_edit_division(request.user, division):
        return redirect("dependency_list", division_id=division.id)

    if request.method == "POST":
        form = DependencyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.division = division
            obj.save()
            return redirect("dependency_list", division_id=division.id)
    else:
        form = DependencyForm()

    return render(request, "dependencies/form.html", {"form": form, "division": division})


@login_required
def dependency_edit(request, pk):
    item = get_object_or_404(Dependency, pk=pk)
    division = item.division

    if not can_edit_division(request.user, division):
        return redirect("dependency_list", division_id=division.id)

    if request.method == "POST":
        form = DependencyForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dependency_list", division_id=division.id)
    else:
        form = DependencyForm(instance=item)

    return render(request, "dependencies/form.html", {"form": form, "division": division})


# ---------------------------------------------------------
# ALTERNATE FACILITIES
# ---------------------------------------------------------

@login_required
def alternate_facility_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = AlternateFacility.objects.filter(division=division)
    return render(request, "alternate_facilities/list.html", {"division": division, "items": items})


@login_required
def alternate_facility_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)

    if not can_edit_division(request.user, division):
        return redirect("alternate_facility_list", division_id=division.id)

    if request.method == "POST":
        form = AlternateFacilityForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.division = division
            obj.save()
            return redirect("alternate_facility_list", division_id=division.id)
    else:
        form = AlternateFacilityForm()

    return render(request, "alternate_facilities/form.html", {"form": form, "division": division})


@login_required
def alternate_facility_edit(request, pk):
    item = get_object_or_404(AlternateFacility, pk=pk)
    division = item.division

    if not can_edit_division(request.user, division):
        return redirect("alternate_facility_list", division_id=division.id)

    if request.method == "POST":
        form = AlternateFacilityForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("alternate_facility_list", division_id=division.id)
    else:
        form = AlternateFacilityForm(instance=item)

    return render(request, "alternate_facilities/form.html", {"form": form, "division": division})


# ---------------------------------------------------------
# COMMUNICATIONS
# ---------------------------------------------------------

@login_required
def communication_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = Communication.objects.filter(division=division)
    return render(request, "communications/list.html", {"division": division, "items": items})


@login_required
def communication_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)

    if not can_edit_division(request.user, division):
        return redirect("communication_list", division_id=division.id)

    if request.method == "POST":
        form = CommunicationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.division = division
            obj.save()
            return redirect("communication_list", division_id=division.id)
    else:
        form = CommunicationForm()

    return render(request, "communications/form.html", {"form": form, "division": division})


@login_required
def communication_edit(request, pk):
    item = get_object_or_404(Communication, pk=pk)
    division = item.division

    if not can_edit_division(request.user, division):
        return redirect("communication_list", division_id=division.id)

    if request.method == "POST":
        form = CommunicationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("communication_list", division_id=division.id)
    else:
        form = CommunicationForm(instance=item)

    return render(request, "communications/form.html", {"form": form, "division": division})


# ---------------------------------------------------------
# RECOVERY PRIORITIES
# ---------------------------------------------------------

@login_required
def recovery_priority_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = RecoveryPriority.objects.filter(division=division)
    return render(request, "recovery_priorities/list.html", {"division": division, "items": items})


@login_required
def recovery_priority_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)

    if not can_edit_division(request.user, division):
        return redirect("recovery_priority_list", division_id=division.id)

    if request.method == "POST":
        form = RecoveryPriorityForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.division = division
            obj.save()
            return redirect("recovery_priority_list", division_id=division.id)
    else:
        form = RecoveryPriorityForm()

    return render(request, "recovery_priorities/form.html", {"form": form, "division": division})


@login_required
def recovery_priority_edit(request, pk):
    item = get_object_or_404(RecoveryPriority, pk=pk)
    division = item.division

    if not can_edit_division(request.user, division):
        return redirect("recovery_priority_list", division_id=division.id)

    if request.method == "POST":
        form = RecoveryPriorityForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("recovery_priority_list", division_id=division.id)
    else:
        form = RecoveryPriorityForm(instance=item)

    return render(request, "recovery_priorities/form.html", {"form": form, "division": division})


# ---------------------------------------------------------
# DIVISION METADATA
# ---------------------------------------------------------

@login_required
def division_metadata_detail(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    metadata = get_object_or_404(DivisionMetadata, division=division)
    return render(request, "division_metadata/detail.html", {"division": division, "metadata": metadata})


@login_required
def division_metadata_edit(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    metadata = get_object_or_404(DivisionMetadata, division=division)

    if not can_edit_division(request.user, division):
        return redirect("division_metadata_detail", division_id=division.id)

    if request.method == "POST":
        form = DivisionMetadataForm(request.POST, instance=metadata)
        if form.is_valid():
            form.save()
            return redirect("division_metadata_detail", division_id=division.id)
    else:
        form = DivisionMetadataForm(instance=metadata)

    return render(request, "division_metadata/form.html", {"form": form, "division": division})


# ---------------------------------------------------------
# COOP PLAN GENERATION
# ---------------------------------------------------------

@login_required
def generate_coop_plan_view(request, division_id):
    division = get_object_or_404(Division, pk=division_id)

    if not can_edit_division(request.user, division):
        return redirect("division_detail", pk=division.id)

    if request.method == "POST":
        result = generate_coop_plan_for_division(division.id)
        return render(request, "coop_plan/generate_result.html", {"division": division, "result": result})

    return redirect("division_detail", pk=division.id)


# ---------------------------------------------------------
# PLAN HISTORY
# ---------------------------------------------------------

@login_required
def coop_plan_history(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    plans = GeneratedPlan.objects.filter(division=division).order_by("-created_at")
    return render(request, "coop_plan/history.html", {"division": division, "plans": plans})

# ---------------------------------------------------------
# Service Now API
# ---------------------------------------------------------

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .integrations.servicenow import sync_critical_applications_from_servicenow
from .models import Division
from .views import can_edit_division  # if defined there

@login_required
def sync_critical_applications_servicenow(request, division_id):
    division = get_object_or_404(Division, pk=division_id)

    if not can_edit_division(request.user, division):
        messages.error(request, "You do not have permission to sync this division.")
        return redirect("critical_application_list", division_id=division.id)

    # Optional: allow a query filter via GET or POST
    query = request.GET.get("query") or None

    summary = sync_critical_applications_from_servicenow(division, query=query)
    messages.success(
        request,
        f"ServiceNow sync complete: {summary['created']} created, {summary['updated']} updated (total {summary['total']}).",
    )
    return redirect("critical_application_list", division_id=division.id)

