from rest_framework import serializers
from .models import Flight, Passenger

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PassengerSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)  # Nested flight details

    class Meta:
        model = Passenger
        fields = '__all__'
