from django.contrib import admin

from gro_api.actuators.models import ActuatorType, ControlProfile, Actuator, ActuatorState, ActuatorEffect


class ActuatorTypeAdmin(admin.ModelAdmin):
    pass


class ControlProfileAdmin(admin.ModelAdmin):
    pass


class ActuatorEffectAdmin(admin.ModelAdmin):
    pass


class ActuatorAdmin(admin.ModelAdmin):
    pass


class ActuatorStateAdmin(admin.ModelAdmin):
    pass


admin.site.register(ActuatorType, ActuatorTypeAdmin)
admin.site.register(ControlProfile, ControlProfileAdmin)
admin.site.register(ActuatorEffect, ActuatorEffectAdmin)
admin.site.register(Actuator, ActuatorAdmin)
admin.site.register(ActuatorState, ActuatorStateAdmin)

