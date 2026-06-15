from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('receipt/<int:booking_id>/', views.generate_receipt, name='generate_receipt'),
    path('advisory/<int:booking_id>/', views.generate_advisory, name='generate_advisory'),
]
