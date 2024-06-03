
from django.shortcuts import render
#from .models import Car



# def home(request):
#    cars=Car.objects.all()
#    return render(request, 'cars/home.html', {'cars': cars})



def home(request):
   
    return render(request, 'home.html')

def car_details(request):
   
    return render(request, 'car_details.html')


