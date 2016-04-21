from django.contrib import admin

from gro_api.recipes.models import Recipe, RecipeRun, SetPoint, ActuatorOverride

admin.site.register(Recipe)
admin.site.register(RecipeRun)
admin.site.register(SetPoint)
admin.site.register(ActuatorOverride)

