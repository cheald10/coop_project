from django import forms
from .models import (
    Division, EssentialFunction, CriticalApplication, KeyPersonnel,
    VitalRecord, Dependency, AlternateFacility, Communication,
    RecoveryPriority, DivisionMetadata
)

class EssentialFunctionForm(forms.ModelForm):
    class Meta:
        model = EssentialFunction
        fields = '__all__'


class CriticalApplicationForm(forms.ModelForm):
    class Meta:
        model = CriticalApplication
        fields = '__all__'


class KeyPersonnelForm(forms.ModelForm):
    class Meta:
        model = KeyPersonnel
        fields = '__all__'


class VitalRecordForm(forms.ModelForm):
    class Meta:
        model = VitalRecord
        fields = '__all__'


class DependencyForm(forms.ModelForm):
    class Meta:
        model = Dependency
        fields = '__all__'


class AlternateFacilityForm(forms.ModelForm):
    class Meta:
        model = AlternateFacility
        fields = '__all__'


class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communication
        fields = '__all__'


class RecoveryPriorityForm(forms.ModelForm):
    class Meta:
        model = RecoveryPriority
        fields = '__all__'


class DivisionMetadataForm(forms.ModelForm):
    class Meta:
        model = DivisionMetadata
        fields = '__all__'
