from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import (
    Division, EssentialFunction, CriticalApplication, KeyPersonnel,
    VitalRecord, Dependency, AlternateFacility, Communication,
    RecoveryPriority, DivisionMetadata
)
from .serializers import (
    DivisionSerializer, EssentialFunctionSerializer, CriticalApplicationSerializer,
    KeyPersonnelSerializer, VitalRecordSerializer, DependencySerializer,
    AlternateFacilitySerializer, CommunicationSerializer,
    RecoveryPrioritySerializer, DivisionMetadataSerializer
)


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Admins and superusers: full access.
    Leadership + authenticated: read-only.
    Everyone else: deny.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            # read-only allowed for any authenticated user
            return True
        # write operations: admin only
        return (
            request.user.is_superuser
            or request.user.groups.filter(name="COOP Admins").exists()
        )


class IsCoordinatorForDivision(permissions.BasePermission):
    """
    Coordinators can only write to their own division's data.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser or request.user.groups.filter(name="COOP Admins").exists():
            return True
        if request.user.groups.filter(name="Coordinators").exists():
            division = getattr(obj, "division", obj if isinstance(obj, Division) else None)
            return division and division.coordinator == request.user
        return False


class BaseSecureViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly, IsCoordinatorForDivision]


class DivisionViewSet(BaseSecureViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer


class EssentialFunctionViewSet(BaseSecureViewSet):
    queryset = EssentialFunction.objects.all()
    serializer_class = EssentialFunctionSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        division_id = self.request.query_params.get("division")
        if division_id:
            qs = qs.filter(division_id=division_id)
        return qs


class CriticalApplicationViewSet(BaseSecureViewSet):
    queryset = CriticalApplication.objects.all()
    serializer_class = CriticalApplicationSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        division_id = self.request.query_params.get("division")
        if division_id:
            qs = qs.filter(division_id=division_id)
        return qs


class KeyPersonnelViewSet(BaseSecureViewSet):
    queryset = KeyPersonnel.objects.all()
    serializer_class = KeyPersonnelSerializer


class VitalRecordViewSet(BaseSecureViewSet):
    queryset = VitalRecord.objects.all()
    serializer_class = VitalRecordSerializer


class DependencyViewSet(BaseSecureViewSet):
    queryset = Dependency.objects.all()
    serializer_class = DependencySerializer


class AlternateFacilityViewSet(BaseSecureViewSet):
    queryset = AlternateFacility.objects.all()
    serializer_class = AlternateFacilitySerializer


class CommunicationViewSet(BaseSecureViewSet):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer


class RecoveryPriorityViewSet(BaseSecureViewSet):
    queryset = RecoveryPriority.objects.all()
    serializer_class = RecoveryPrioritySerializer


class DivisionMetadataViewSet(BaseSecureViewSet):
    queryset = DivisionMetadata.objects.all()
    serializer_class = DivisionMetadataSerializer
