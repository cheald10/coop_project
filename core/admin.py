from django.contrib import admin
from .models import (
    Division, EssentialFunction, CriticalApplication, KeyPersonnel,
    VitalRecord, Dependency, AlternateFacility, Communication,
    RecoveryPriority, DivisionMetadata, GeneratedPlan,
    ServiceNowIntegrationConfig
)

admin.site.register(Division)
admin.site.register(EssentialFunction)
admin.site.register(CriticalApplication)
admin.site.register(KeyPersonnel)
admin.site.register(VitalRecord)
admin.site.register(Dependency)
admin.site.register(AlternateFacility)
admin.site.register(Communication)
admin.site.register(RecoveryPriority)
admin.site.register(DivisionMetadata)
admin.site.register(GeneratedPlan)
admin.site.register(ServiceNowIntegrationConfig)
