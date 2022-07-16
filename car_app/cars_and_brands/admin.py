from nis import cat
from django.contrib import admin
from cars_and_brands.models import CarBrand, CarModel

# Register your models here.
admin.site.register(CarBrand)
admin.site.register(CarModel)