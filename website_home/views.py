from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, "home.html")

def facilities_products(request):
    return render(request, "facilities_products.html")

def about_us(request):
    return render(request, "about_us.html")

def contact_us(request):

    if request.method=="POST":
        myFName = request.POST['myFName']
        myLName = request.POST['myLName']
        myEmail = request.POST['myEmail']
        contact_number = request.POST['contact_number']
        description = request.POST['description']
        description+=f"\n Email of {myFName} {myLName} : {myEmail}"
        description+=f"\n contact Number : {contact_number}"
        
        send_mail(
            f'{myFName} {myLName} wants to contact you', #subject
            description, #message
            myEmail, #from email
            ['nipunpatel2002@gmail.com'], #To email
        )

        return render(request, "contact_us.html")

    return render(request, "contact_us.html")


def condensers(request):
    return render(request, "products/condensers.html")

def tyre_recycling_plant(request):
    return render(request, "products/tyre_recycling_plant.html")

def heat_exchangers(request):
    return render(request, "products/heat_exchangers.html")

def industrial_storage_tanks(request):
    return render(request, "products/industrial_storage_tanks.html")

def pressure_vessels(request):
    return render(request, "products/pressure_vessels.html")

def chimeny(request):
    return render(request, "products/chimeny.html")

def industrial_reactors(request):
    return render(request, "products/industrial_reactors.html")

def industrial_fabrication_service(request):
    return render(request, "products/industrial_fabrication_service.html")