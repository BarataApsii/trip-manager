import os
from django.conf import settings
from django.template.loader import render_to_string
from weasyprint import HTML


def generate_receipt_pdf(booking):
    payment = booking.payment
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'logo.png')
    context = {
        'booking': booking,
        'customer': booking.customer,
        'payment': payment,
        'logo_path': logo_path,
    }
    html_string = render_to_string('documents/receipt_template.html', context)
    base_url = str(settings.BASE_DIR)
    pdf_bytes = HTML(string=html_string, base_url=base_url).write_pdf()
    return pdf_bytes


def generate_advisory_pdf(booking):
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'logo.png')
    context = {
        'booking': booking,
        'customer': booking.customer,
        'logo_path': logo_path,
    }
    html_string = render_to_string('documents/advisory_template.html', context)
    base_url = str(settings.BASE_DIR)
    pdf_bytes = HTML(string=html_string, base_url=base_url).write_pdf()
    return pdf_bytes
