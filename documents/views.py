from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from bookings.models import Booking
from .pdf_generator import generate_receipt_pdf, generate_advisory_pdf


def generate_receipt(request, booking_id):
    booking = get_object_or_404(
        Booking.objects.select_related('customer', 'payment'), pk=booking_id
    )
    pdf_bytes = generate_receipt_pdf(booking)
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    filename = f"receipt_{booking.pnr}.pdf"
    response['Content-Disposition'] = f'inline; filename="{filename}"'
    return response


def generate_advisory(request, booking_id):
    booking = get_object_or_404(
        Booking.objects.select_related('customer', 'payment'), pk=booking_id
    )
    pdf_bytes = generate_advisory_pdf(booking)
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    filename = f"travel_advisory_{booking.pnr}.pdf"
    response['Content-Disposition'] = f'inline; filename="{filename}"'
    return response
