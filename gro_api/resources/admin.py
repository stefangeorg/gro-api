from django.contrib import admin

from gro_api.resources.models import ResourceType, ResourceProperty, ResourceEffect, Resource

admin.site.register(ResourceType)
admin.site.register(ResourceProperty)
admin.site.register(ResourceEffect)
admin.site.register(Resource)
