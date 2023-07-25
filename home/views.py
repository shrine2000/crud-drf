from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request):
    car = {
        'suv': ['Innova', 'Endeavour', 'XUV700'],
        'sedan': ['honda city', 'VW Vitrus', 'Verna'],
        'hatchback': ['Polo', 'Swift']
    }
    return Response(car)