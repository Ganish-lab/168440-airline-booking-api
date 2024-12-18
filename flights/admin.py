from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Flight, Passenger

# Register the Flight model
@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'origin', 'destination', 'departure', 'arrival', 'capacity')
    search_fields = ('flight_number', 'origin', 'destination')
    list_filter = ('departure', 'arrival')

# Register the Passenger model
@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'flight')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('flight',)
