from django.shortcuts import render, get_object_or_404, redirect
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
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.db.models import Count from .models import Division, EssentialFunction, CriticalApplication

# -------------------------
# Division Views
# -------------------------

def division_list(request):
    divisions = Division.objects.all()
    return render(request, "divisions/list.html", {"divisions": divisions})


def division_detail(request, pk):
    division = get_object_or_404(Division, pk=pk)
    return render(request, "divisions/detail.html", {"division": division})


# -------------------------
# Essential Functions
# -------------------------

def essential_function_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = EssentialFunction.objects.filter(division=division)
    return render(request, "essential_functions/list.html", {"division": division, "items": items})


def essential_function_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    if request.method == "POST":
        form = EssentialFunctionForm(request.POST)
        if form.is_valid():
            ef = form.save(commit=False)
            ef.division = division
            ef.save()
            return redirect("essential_function_list", division_id=division.id)
    else:
        form = EssentialFunctionForm()
    return render(request, "essential_functions/form.html", {"form": form, "division": division})


def essential_function_edit(request, pk):
    item = get_object_or_404(EssentialFunction, pk=pk)
    division = item.division
    if request.method == "POST":
        form = EssentialFunctionForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("essential_function_list", division_id=division.id)
    else:
        form = EssentialFunctionForm(instance=item)
    return render(request, "essential_functions/form.html", {"form": form, "division": division})


# -------------------------
# Critical Applications
# -------------------------

def critical_application_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = CriticalApplication.objects.filter(division=division)
    return render(request, "critical_applications/list.html", {"division": division, "items": items})


def critical_application_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
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


def critical_application_edit(request, pk):
    item = get_object_or_404(CriticalApplication, pk=pk)
    division = item.division
    if request.method == "POST":
        form = CriticalApplicationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("critical_application_list", division_id=division.id)
    else:
        form = CriticalApplicationForm(instance=item)
    return render(request, "critical_applications/form.html", {"form": form, "division": division})


# -------------------------
# Key Personnel
# -------------------------

def key_personnel_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = KeyPersonnel.objects.filter(division=division)
    return render(request, "key_personnel/list.html", {"division": division, "items": items})


def key_personnel_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
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


def key_personnel_edit(request, pk):
    item = get_object_or_404(KeyPersonnel, pk=pk)
    division = item.division
    if request.method == "POST":
        form = KeyPersonnelForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("key_personnel_list", division_id=division.id)
    else:
        form = KeyPersonnelForm(instance=item)
    return render(request, "key_personnel/form.html", {"form": form, "division": division})


# -------------------------
# Vital Records
# -------------------------

def vital_record_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = VitalRecord.objects.filter(division=division)
    return render(request, "vital_records/list.html", {"division": division, "items": items})


def vital_record_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
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


def vital_record_edit(request, pk):
    item = get_object_or_404(VitalRecord, pk=pk)
    division = item.division
    if request.method == "POST":
        form = VitalRecordForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("vital_record_list", division_id=division.id)
    else:
        form = VitalRecordForm(instance=item)
    return render(request, "vital_records/form.html", {"form": form, "division": division})


# -------------------------
# Dependencies
# -------------------------

def dependency_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = Dependency.objects.filter(division=division)
    return render(request, "dependencies/list.html", {"division": division, "items": items})


def dependency_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
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


def dependency_edit(request, pk):
    item = get_object_or_404(Dependency, pk=pk)
    division = item.division
    if request.method == "POST":
        form = DependencyForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dependency_list", division_id=division.id)
    else:
        form = DependencyForm(instance=item)
    return render(request, "dependencies/form.html", {"form": form, "division": division})


# -------------------------
# Alternate Facilities
# -------------------------

def alternate_facility_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = AlternateFacility.objects.filter(division=division)
    return render(request, "alternate_facilities/list.html", {"division": division, "items": items})


def alternate_facility_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
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


def alternate_facility_edit(request, pk):
    item = get_object_or_404(AlternateFacility, pk=pk)
    division = item.division
    if request.method == "POST":
        form = AlternateFacilityForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("alternate_facility_list", division_id=division.id)
    else:
        form = AlternateFacilityForm(instance=item)
    return render(request, "alternate_facilities/form.html", {"form": form, "division": division})


# -------------------------
# Communications
# -------------------------

def communication_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = Communication.objects.filter(division=division)
    return render(request, "communications/list.html", {"division": division, "items": items})


def communication_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
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


def communication_edit(request, pk):
    item = get_object_or_404(Communication, pk=pk)
    division = item.division
    if request.method == "POST":
        form = CommunicationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("communication_list", division_id=division.id)
    else:
        form = CommunicationForm(instance=item)
    return render(request, "communications/form.html", {"form": form, "division": division})


# -------------------------
# Recovery Priorities
# -------------------------

def recovery_priority_list(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    items = RecoveryPriority.objects.filter(division=division)
    return render(request, "recovery_priorities/list.html", {"division": division, "items": items})


def recovery_priority_create(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
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


def recovery_priority_edit(request, pk):
    item = get_object_or_404(RecoveryPriority, pk=pk)
    division = item.division
    if request.method == "POST":
        form = RecoveryPriorityForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("recovery_priority_list", division_id=division.id)
    else:
        form = RecoveryPriorityForm(instance=item)
    return render(request, "recovery_priorities/form.html", {"form": form, "division": division})


# -------------------------
# Division Metadata
# -------------------------

def division_metadata_detail(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    metadata = get_object_or_404(DivisionMetadata, division=division)
    return render(request, "division_metadata/detail.html", {"division": division, "metadata": metadata})


def division_metadata_edit(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    metadata = get_object_or_404(DivisionMetadata, division=division)
    if request.method == "POST":
        form = DivisionMetadataForm(request.POST, instance=metadata)
        if form.is_valid():
            form.save()
            return redirect("division_metadata_detail", division_id=division.id)
    else:
        form = DivisionMetadataForm(instance=metadata)
    return render(request, "division_metadata/form.html", {"form": form, "division": division})


# -------------------------
# COOP Plan Generation
# -------------------------

def generate_coop_plan_view(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    if request.method == "POST":
        result = generate_coop_plan_for_division(division.id)
        return render(request, "coop_plan/generate_result.html", {"division": division, "result": result})
    return redirect("division_detail", pk=division.id)


def coop_plan_history(request, division_id):
    division = get_object_or_404(Division, pk=division_id)
    plans = GeneratedPlan.objects.filter(division=division).order_by("-created_at")
    return render(request, "coop_plan/history.html", {"division": division, "plans": plans})

# -------------------------
# Leadership Dashboard
# -------------------------

def is_leadership(user):
    return user.is_authenticated and (user.is_superuser or user.groups.filter(name="Leadership").exists())

@login_required
@user_passes_test(is_leadership)
def leadership_dashboard(request):
    divisions = (
        Division.objects
        .all()
        .annotate(
            essential_function_count=Count("essentialfunction"),
            critical_application_count=Count("criticalapplication"),
        )
        .order_by("name")
    )

    return render(request, "dashboard/leadership.html", {"divisions": divisions})
