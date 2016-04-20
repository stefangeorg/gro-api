from django.contrib import admin

from gro_api.sensors.models import DataPoint, SensingPoint, Sensor, SensorType

admin.site.register(SensorType)
admin.site.register(Sensor)
admin.site.register(SensingPoint)
admin.site.register(DataPoint)