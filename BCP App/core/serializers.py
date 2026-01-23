from rest_framework import serializers
from .models import *

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class EssentialFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EssentialFunction
        fields = '__all__'

class CriticalApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriticalApplication
        fields = '__all__'

class KeyPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyPersonnel
        fields = '__all__'

class VitalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalRecord
        fields = '__all__'

class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependency
        fields = '__all__'

class AlternateFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AlternateFacility
        fields = '__all__'

class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = '__all__'

class RecoveryPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecoveryPriority
        fields = '__all__'

class DivisionMetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisionMetadata
        fields = '__all__'