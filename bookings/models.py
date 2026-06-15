from django.db import models
from customers.models import Customer


class Booking(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='bookings'
    )
    pnr = models.CharField(max_length=20, verbose_name='PNR')
    ticket_number = models.CharField(max_length=50, blank=True, null=True)
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=20, blank=True, null=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    departure_time = models.TimeField(blank=True, null=True)
    arrival_date = models.DateField(blank=True, null=True)
    arrival_time = models.TimeField(blank=True, null=True)
    booking_class = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='confirmed'
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-departure_date']

    def __str__(self):
        return f"{self.pnr} - {self.customer.full_name} ({self.origin} → {self.destination})"

    @property
    def route(self):
        return f"{self.origin} → {self.destination}"
