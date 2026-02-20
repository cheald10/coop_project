from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from core import api

router = DefaultRouter()
router.register(r"divisions", api.DivisionViewSet)
router.register(r"essential-functions", api.EssentialFunctionViewSet)
router.register(r"critical-applications", api.CriticalApplicationViewSet)
router.register(r"key-personnel", api.KeyPersonnelViewSet)
router.register(r"vital-records", api.VitalRecordViewSet)
router.register(r"dependencies", api.DependencyViewSet)
router.register(r"alternate-facilities", api.AlternateFacilityViewSet)
router.register(r"communications", api.CommunicationViewSet)
router.register(r"recovery-priorities", api.RecoveryPriorityViewSet)
router.register(r"division-metadata", api.DivisionMetadataViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("api/v1/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
    path("", include("app.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
