
from django.shortcuts import render
#from .models import Car



# def home(request):
#    cars=Car.objects.all()
#    return render(request, 'cars/home.html', {'cars': cars})



def home(request):
   
    return render(request, 'cars/home.html')

def car(request):
   
    return render(request, 'cars/car.html')


