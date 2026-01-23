from django.urls import path, include
from rest_framework import routers
from .api import (
    DivisionViewSet, EssentialFunctionViewSet, CriticalApplicationViewSet,
    KeyPersonnelViewSet, VitalRecordViewSet, DependencyViewSet,
    AlternateFacilityViewSet, CommunicationViewSet, RecoveryPriorityViewSet,
    DivisionMetadataViewSet
)

router = routers.DefaultRouter()
router.register(r'divisions', DivisionViewSet)
router.register(r'essential-functions', EssentialFunctionViewSet)
router.register(r'critical-applications', CriticalApplicationViewSet)
router.register(r'key-personnel', KeyPersonnelViewSet)
router.register(r'vital-records', VitalRecordViewSet)
router.register(r'dependencies', DependencyViewSet)
router.register(r'alternate-facilities', AlternateFacilityViewSet)
router.register(r'communications', CommunicationViewSet)
router.register(r'recovery-priorities', RecoveryPriorityViewSet)
router.register(r'division-metadata', DivisionMetadataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]