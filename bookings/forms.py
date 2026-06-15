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
        labels = {
            'customer': 'Traveller',
            'pnr': 'Booking Reference (PNR)',
            'ticket_number': 'Ticket Number',
            'airline': 'Airline',
            'flight_number': 'Flight Number',
            'origin': 'Departure Location',
            'destination': 'Arrival Location',
            'departure_date': 'Departure Date',
            'departure_time': 'Departure Time',
            'arrival_date': 'Arrival Date',
            'arrival_time': 'Arrival Time',
            'booking_class': 'Class',
            'status': 'Booking Status',
            'notes': 'Notes',
        }
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-select'}),
            'pnr': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. ABC123'}),
            'ticket_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 081-1234567890'}),
            'airline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Air Niugini'}),
            'flight_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. PX100'}),
            'origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Port Moresby'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Madang'}),
            'departure_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'departure_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'arrival_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'arrival_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'booking_class': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Any additional notes...'}),
        }
