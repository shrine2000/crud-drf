from home.views import vehicle, vehicle_detail
from django.urls import path

urlpatterns = [
    path('vehicle/', vehicle),
    path('vehicle/<int:pk>/', vehicle_detail),
]
