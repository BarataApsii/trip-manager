from django.db import models
from bookings.models import Booking


class Document(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('receipt', 'Receipt'),
        ('travel_advisory', 'Travel Advisory'),
    ]

    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='documents'
    )
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPE_CHOICES)
    file = models.FileField(upload_to='documents/', blank=True, null=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-generated_at']

    def __str__(self):
        return f"{self.get_document_type_display()} - {self.booking.pnr}"
