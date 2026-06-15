import os
from django.conf import settings
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO


def generate_receipt_pdf(booking):
    payment = booking.payment
    context = {
        'booking': booking,
        'customer': booking.customer,
        'payment': payment,
        'logo_path': logo_path,
    }

    html_string = render_to_string('documents/receipt_template.html', context)
    pdf_bytes = HTML(string=html_string).write_pdf()
    return pdf_bytes


def generate_advisory_pdf(booking):
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'logo.png')
    context = {
        'booking': booking,
        'customer': booking.customer,
        'logo_path': logo_path,
    }

    html_string = render_to_string('documents/advisory_template.html', context)
    pdf_bytes = HTML(string=html_string).write_pdf()
    return pdf_bytes
