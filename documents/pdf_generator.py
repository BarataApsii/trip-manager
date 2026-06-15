from django.template.loader import render_to_string
from xhtml2pdf import pisa
from io import BytesIO


def generate_receipt_pdf(booking):
    payment = booking.payment

    context = {
        'booking': booking,
        'customer': booking.customer,
        'payment': payment,
    }

    html_string = render_to_string('documents/receipt_template.html', context)

    result = BytesIO()
    pdf = pisa.pisaDocument(
        BytesIO(html_string.encode("UTF-8")),
        result
    )

    if pdf.err:
        return None

    return result.getvalue()


def generate_advisory_pdf(booking):
    context = {
        'booking': booking,
        'customer': booking.customer,
    }

    html_string = render_to_string('documents/advisory_template.html', context)

    result = BytesIO()
    pdf = pisa.pisaDocument(
        BytesIO(html_string.encode("UTF-8")),
        result
    )

    if pdf.err:
        return None

    return result.getvalue()