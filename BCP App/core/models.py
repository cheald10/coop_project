from django.db import models
from django.contrib.auth.models import User


class Division(models.Model):
    name = models.CharField(max_length=255, unique=True)
    coordinator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="division_coordinator")
    plan_status = models.CharField(max_length=50, default="Draft")
    last_updated = models.DateField(auto_now=True)
    next_review_date = models.DateField(null=True, blank=True)
    plan_version = models.IntegerField(default=1)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class EssentialFunction(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    mtd = models.CharField(max_length=50)
    rto = models.CharField(max_length=50)
    owner = models.CharField(max_length=255, blank=True)
    dependencies = models.TextField(blank=True)
    alternate_procedures = models.TextField(blank=True)
    priority = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CriticalApplication(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    hosting_environment = models.CharField(max_length=50)
    recovery_tier = models.CharField(max_length=50)
    rto = models.CharField(max_length=50)
    vendor_contact = models.CharField(max_length=255, blank=True)
    dependencies = models.TextField(blank=True)
    workarounds = models.TextField(blank=True)

    def __str__(self):
        return self.name


class KeyPersonnel(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    primary_or_alternate = models.CharField(max_length=50)
    work_phone = models.CharField(max_length=50, blank=True)
    mobile_phone = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class VitalRecord(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    record_type = models.CharField(max_length=50)
    storage_location = models.CharField(max_length=255)
    backup_location = models.CharField(max_length=255)
    format = models.CharField(max_length=50)
    owner = models.CharField(max_length=255, blank=True)
    priority = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Dependency(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dependency_type = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    criticality = models.CharField(max_length=50)
    vendor_contact = models.CharField(max_length=255, blank=True)
    recovery_notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class AlternateFacility(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    facility_type = models.CharField(max_length=50)
    capacity = models.IntegerField()
    it_availability = models.CharField(max_length=50)
    contact = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Communication(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    communication_type = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    primary_contact = models.CharField(max_length=255)
    contact_details = models.TextField()
    backup_contact = models.CharField(max_length=255, blank=True)
    method = models.CharField(max_length=50)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.communication_type} - {self.division.name}"


class RecoveryPriority(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=50)
    priority_level = models.IntegerField()
    rationale = models.TextField(blank=True)

    def __str__(self):
        return f"{self.item_name} (P{self.priority_level})"


class DivisionMetadata(models.Model):
    division = models.OneToOneField(Division, on_delete=models.CASCADE)
    director = models.CharField(max_length=255)
    coordinator = models.CharField(max_length=255, blank=True)
    mission_statement = models.TextField(blank=True)
    primary_location = models.TextField(blank=True)
    staff_count = models.IntegerField(default=0)
    hours_of_operation = models.CharField(max_length=255, blank=True)
    critical_services_summary = models.TextField(blank=True)
    leadership_contact_info = models.TextField(blank=True)

    def __str__(self):
        return f"Metadata for {self.division.name}"