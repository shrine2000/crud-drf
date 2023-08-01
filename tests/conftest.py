import pytest
from rest_framework.test import APIClient
from home.models import Car


@pytest.fixture()
def car_1(db):
    return Car.objects.create(make="Tesla", year=2019)


@pytest.fixture
def car_2(db):
    return Car.objects.create(make="Ford", year=2015)


@pytest.fixture
def api_client():
    return APIClient()
