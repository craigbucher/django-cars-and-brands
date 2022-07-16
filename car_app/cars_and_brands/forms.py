from django.forms import ModelForm
from cars_and_brands.models import CarBrand, CarModel

class CarBrandForm(ModelForm):
    class Meta:
        model = CarBrand
        fields = "__all__"

class CarModelForm(ModelForm):
    class Meta:
        model = CarModel
        fields = "__all__"