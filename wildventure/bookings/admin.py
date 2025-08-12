from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "destination", "number_of_people", "travel_date", "budget")
    list_filter = ("destination", "accommodation", "budget")
    search_fields = ("name", "email")
