from django.shortcuts import render
from django.http import HttpResponse
from cars_and_brands.models import CarBrand, CarModel

# Create your views here.
def index(request):
    return HttpResponse('Home Page')

# brand
def brands(request):
    data = {
        "brands": CarBrand.objects.all()
    }
    return render(request, "pages/brands/brand_list.html", data)

def brand_new(request):
    pass

def brand_detail(request, brand_id):
    pass

def brand_edit(request, brand_id):
    pass

# models   
def models(request, brand_id):
    pass

def model_new(request, brand_id):
    pass

def model_detail(request, brand_id, model_id):
    pass

def model_edit(request, brand_id, model_id):
    pass