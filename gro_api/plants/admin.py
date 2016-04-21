from django.contrib import admin

from gro_api.plants.models import PlantModel, PlantType, Plant, SowEvent, TransferEvent, HarvestEvent, PlantComment

admin.site.register(PlantComment)
admin.site.register(HarvestEvent)
admin.site.register(TransferEvent)
admin.site.register(SowEvent)
admin.site.register(Plant)
admin.site.register(PlantType)
admin.site.register(PlantModel)