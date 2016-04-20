from django.contrib import admin

from gro_api.layout.models import Model3D, TrayLayout, PlantSiteLayout, Enclosure, Tray, PlantSite


admin.site.register(Model3D)
admin.site.register(TrayLayout)
admin.site.register(PlantSiteLayout)
admin.site.register(Enclosure)
admin.site.register(Tray)
admin.site.register(PlantSite)