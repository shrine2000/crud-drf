from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'  # Include all fields of the Car model
        # fields = ['year', 'make']  # Include only 'year' and 'make' fields from the Car model
        # use exclude = ['make'] to remove certain fields when using '__all__'

    def validate_year(self, value):
        if value < 1900 or value > 2025:
            raise serializers.ValidationError("Year must be between 1900 and 2025")
        return value

    def update(self, instance, validated_data):
        instance.make = validated_data.get('make', instance.make)
        instance.year = validated_data.get('year', instance.year)
        instance.save()
        return instance

    def create(self, validated_data):
        car = Car.objects.create(**validated_data)
        return car
