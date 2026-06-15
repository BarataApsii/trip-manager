from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['pnr', 'customer', 'airline', 'origin', 'destination', 'departure_date', 'status']
    search_fields = ['pnr', 'customer__first_name', 'customer__last_name', 'destination']
    list_filter = ['status', 'airline', 'departure_date']
