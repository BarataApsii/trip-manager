from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from payments.forms import PaymentForm
from payments.models import Payment


def booking_list(request):
    bookings = Booking.objects.select_related('customer', 'payment').all()
    query = request.GET.get('q', '')
    if query:
        bookings = bookings.filter(
            pnr__icontains=query
        ) | bookings.filter(
            customer__first_name__icontains=query
        ) | bookings.filter(
            customer__last_name__icontains=query
        ) | bookings.filter(
            destination__icontains=query
        )
    return render(request, 'bookings/booking_list.html', {
        'bookings': bookings,
        'query': query,
    })


def booking_detail(request, pk):
    booking = get_object_or_404(
        Booking.objects.select_related('customer', 'payment'), pk=pk
    )
    return render(request, 'bookings/booking_detail.html', {
        'booking': booking,
    })


def booking_create(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        payment_form = PaymentForm(request.POST)
        if booking_form.is_valid() and payment_form.is_valid():
            booking = booking_form.save()
            payment = payment_form.save(commit=False)
            payment.booking = booking
            payment.save()
            messages.success(request, f'Booking "{booking.pnr}" created successfully.')
            return redirect('bookings:booking_detail', pk=booking.pk)
    else:
        booking_form = BookingForm()
        payment_form = PaymentForm()
    return render(request, 'bookings/booking_form.html', {
        'booking_form': booking_form,
        'payment_form': payment_form,
        'title': 'New Booking',
    })


def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    try:
        payment = booking.payment
    except Payment.DoesNotExist:
        payment = None

    if request.method == 'POST':
        booking_form = BookingForm(request.POST, instance=booking)
        payment_form = PaymentForm(request.POST, instance=payment)
        if booking_form.is_valid() and payment_form.is_valid():
            booking = booking_form.save()
            payment = payment_form.save(commit=False)
            payment.booking = booking
            payment.save()
            messages.success(request, f'Booking "{booking.pnr}" updated successfully.')
            return redirect('bookings:booking_detail', pk=booking.pk)
    else:
        booking_form = BookingForm(instance=booking)
        payment_form = PaymentForm(instance=payment)
    return render(request, 'bookings/booking_form.html', {
        'booking_form': booking_form,
        'payment_form': payment_form,
        'title': 'Edit Booking',
        'booking': booking,
    })


def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking deleted successfully.')
        return redirect('bookings:booking_list')
    return render(request, 'bookings/booking_confirm_delete.html', {
        'booking': booking,
    })
