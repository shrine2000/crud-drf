import pytest
from rest_framework.test import APIClient
from rest_framework import status
from home.models import Car

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_vehicle_get(api_client):
    car1 = Car.objects.create(make="Tesla", year=2019)
    car2 = Car.objects.create(make="Ford", year=2015)

    response = api_client.get('/api/vehicle/')
    print(response.data)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

    response_data = [dict(item) for item in response.data]

    assert response_data == [
        {
            "id": car1.id,
            "make": "Tesla",
            "year": 2019,
        },
        {
            "id": car2.id,
            "make": "Ford",
            "year": 2015,
        },
    ]
