from django.template.loader import render_to_string
from weasyprint import HTML


def generate_receipt_pdf(booking):
    payment = booking.payment
    context = {
        'booking': booking,
        'customer': booking.customer,
        'payment': payment,
    }
    html_string = render_to_string('documents/receipt_template.html', context)
    pdf_bytes = HTML(string=html_string).write_pdf()
    return pdf_bytes


def generate_advisory_pdf(booking):
    context = {
        'booking': booking,
        'customer': booking.customer,
    }
    html_string = render_to_string('documents/advisory_template.html', context)
    pdf_bytes = HTML(string=html_string).write_pdf()
    return pdf_bytes
