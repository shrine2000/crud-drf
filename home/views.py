from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerializer


# https://www.bezkoder.com/django-rest-api/

@api_view(['GET', 'POST'])
def vehicle(request):
    if request.method == 'GET':
        make = request.GET.get('make')
        if make:
            cars = Car.objects.filter(make=make)
        else:
            cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH', 'DELETE'])
def vehicle_detail(request, pk=None):
    if request.method == 'PUT':
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        if pk is not None:
            car = Car.objects.get(pk=pk)
            serializer = CarSerializer(car, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        try:
            car = Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            return Response({'message': 'Car deleted successfully'}, status=status.HTTP_404_NOT_FOUND)
        car.delete()
        return Response({'message': 'Car deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
