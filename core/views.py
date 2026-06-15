from django.shortcuts import render
from customers.models import Customer
from bookings.models import Booking
from payments.models import Payment


def dashboard(request):
    total_customers = Customer.objects.count()
    total_bookings = Booking.objects.count()
    recent_bookings = Booking.objects.select_related('customer', 'payment')[:5]
    total_revenue = sum(
        p.total for p in Payment.objects.all()
    )
    return render(request, 'core/dashboard.html', {
        'total_customers': total_customers,
        'total_bookings': total_bookings,
        'recent_bookings': recent_bookings,
        'total_revenue': total_revenue,
    })
