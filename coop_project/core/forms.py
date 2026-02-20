from django import forms
from .models import (
    Division, EssentialFunction, CriticalApplication, KeyPersonnel,
    VitalRecord, Dependency, AlternateFacility, Communication,
    RecoveryPriority, DivisionMetadata
)


class EssentialFunctionForm(forms.ModelForm):
    class Meta:
        model = EssentialFunction
        exclude = ["division"]


class CriticalApplicationForm(forms.ModelForm):
    class Meta:
        model = CriticalApplication
        exclude = ["division"]


class KeyPersonnelForm(forms.ModelForm):
    class Meta:
        model = KeyPersonnel
        exclude = ["division"]


class VitalRecordForm(forms.ModelForm):
    class Meta:
        model = VitalRecord
        exclude = ["division"]


class DependencyForm(forms.ModelForm):
    class Meta:
        model = Dependency
        exclude = ["division"]


class AlternateFacilityForm(forms.ModelForm):
    class Meta:
        model = AlternateFacility
        exclude = ["division"]


class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communication
        exclude = ["division"]


class RecoveryPriorityForm(forms.ModelForm):
    class Meta:
        model = RecoveryPriority
        exclude = ["division"]


class DivisionMetadataForm(forms.ModelForm):
    class Meta:
        model = DivisionMetadata
        exclude = ["division"]
