from xml.dom.minidom import CharacterData
from django.db import models

# Create your models here.
class CarBrand(models.Model):
    name = models.CharField(max_length = 64)
    description = models.CharField(max_length = 128)

    def __str__(self):
        return f"brand: {self.name}"
        
class CarModel(models.Model):
    name = models.CharField(max_length = 64)
    brand = models.ForeignKey(CarBrand, related_name="car_models", on_delete=models.CASCADE)

    def __str__(self):
        return f"model: {self.name}, {self.brand}"

