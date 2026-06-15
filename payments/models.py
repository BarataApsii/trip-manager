from django.db import models
from bookings.models import Booking


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('bank_transfer', 'Bank Transfer'),
        ('card', 'Card'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('partial', 'Partial'),
    ]

    booking = models.OneToOneField(
        Booking, on_delete=models.CASCADE, related_name='payment'
    )
    airfare = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    service_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash'
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='paid'
    )
    payment_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment for {self.booking.pnr} - {self.total}"

    @property
    def subtotal(self):
        return self.airfare + self.tax

    @property
    def total(self):
        return self.subtotal + self.service_fee - self.discount
