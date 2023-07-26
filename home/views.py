from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
@api_view(['GET'])
def index(request):
    car = {
        'suv': ['Innova', 'Endeavour', 'XUV700'],
        'sedan': ['honda city', 'VW Vitrus', 'Verna'],
        'hatchback': ['Polo', 'Swift']
    }
    return Response(car)

@api_view(['GET', 'POST'])
def vehicle(request):
    if request.method == 'GET':
        cars = Car.objects.all() # returns query set
        serializer = CarSerializer(cars, many=True) # many=True because we are using taking more than one object
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

