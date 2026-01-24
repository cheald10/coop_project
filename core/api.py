from rest_framework import viewsets
from .models import *
from .serializers import *

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class EssentialFunctionViewSet(viewsets.ModelViewSet):
    queryset = EssentialFunction.objects.all()
    serializer_class = EssentialFunctionSerializer

class CriticalApplicationViewSet(viewsets.ModelViewSet):
    queryset = CriticalApplication.objects.all()
    serializer_class = CriticalApplicationSerializer

class KeyPersonnelViewSet(viewsets.ModelViewSet):
    queryset = KeyPersonnel.objects.all()
    serializer_class = KeyPersonnelSerializer

class VitalRecordViewSet(viewsets.ModelViewSet):
    queryset = VitalRecord.objects.all()
    serializer_class = VitalRecordSerializer

class DependencyViewSet(viewsets.ModelViewSet):
    queryset = Dependency.objects.all()
    serializer_class = DependencySerializer

class AlternateFacilityViewSet(viewsets.ModelViewSet):
    queryset = AlternateFacility.objects.all()
    serializer_class = AlternateFacilitySerializer

class CommunicationViewSet(viewsets.ModelViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer

class RecoveryPriorityViewSet(viewsets.ModelViewSet):
    queryset = RecoveryPriority.objects.all()
    serializer_class = RecoveryPrioritySerializer

class DivisionMetadataViewSet(viewsets.ModelViewSet):
    queryset = DivisionMetadata.objects.all()
    serializer_class = DivisionMetadataSerializer