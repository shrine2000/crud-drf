from home.views import index, vehicle, vehicle_detail
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('index/', index),
    path('vehicle/', vehicle),
    path('vehicle/<int:pk>/', vehicle_detail),
]
