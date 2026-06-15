from django import forms
from .models import Booking
from customers.models import Customer


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'customer', 'pnr', 'ticket_number', 'airline', 'flight_number',
            'origin', 'destination', 'departure_date', 'departure_time',
            'arrival_date', 'arrival_time', 'booking_class', 'status', 'notes',
        ]
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-select'}),
            'pnr': forms.TextInput(attrs={'class': 'form-control'}),
            'ticket_number': forms.TextInput(attrs={'class': 'form-control'}),
            'airline': forms.TextInput(attrs={'class': 'form-control'}),
            'flight_number': forms.TextInput(attrs={'class': 'form-control'}),
            'origin': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'departure_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'departure_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'arrival_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'arrival_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'booking_class': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
