from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def facilities_products(request):
    return render(request, "facilities_products.html")

def about_us(request):
    return render(request, "about_us.html")

def contact_us(request):
    return render(request, "contact_us.html")

def products(request):
    return render(request, "products.html")
