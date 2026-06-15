from django.shortcuts import render
from .models import Payment


def payment_list(request):
    payments = Payment.objects.select_related('booking__customer').all()
    return render(request, 'payments/payment_list.html', {
        'payments': payments,
    })
