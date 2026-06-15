from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['booking', 'airfare', 'tax', 'service_fee', 'total', 'payment_method', 'status']
    search_fields = ['booking__pnr']
    list_filter = ['status', 'payment_method']
