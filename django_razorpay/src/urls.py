from django.urls import path
from .views import payment, payment_status
urlpatterns = [
    path('', payment, name='payment'),
    path('payment-status', payment_status, name='payment-status')
]