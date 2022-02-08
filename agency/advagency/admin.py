from django.contrib import admin

from .models import Employee, Position, AdvertisementType, Place

admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(AdvertisementType)
admin.site.register(Place)


# Register your models here.
