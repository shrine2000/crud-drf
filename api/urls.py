from home.views import index, vehicle
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('vehicle/', vehicle)
]
