import pytest
from rest_framework import status

@pytest.mark.django_db
def test_vehicle_get(api_client, car_1, car_2):
    response = api_client.get('/api/vehicle/')
    print(response.data)

    assert response.status_code == status.HTTP_200_OK
    response_data = [dict(item) for item in response.data]

    assert response_data == [
        {
            "id": car_1.id,
            "make": "Tesla",
            "year": 2019,
        },
        {
            "id": car_2.id,
            "make": "Ford",
            "year": 2015,
        },
    ]
