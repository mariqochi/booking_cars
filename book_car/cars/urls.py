
from django.urls import path
from .import views

# urlpatterns = [
    
#     path ('', views.home)
# ]


urlpatterns = [
    
    path('', views.home, name='home'), 
    path('car_details', views.car_details, name='car_details')    #car_detail=rooms
]