from django.urls import path
from .views import NewBookingView, ThankYouView

app_name = 'bookings'

urlpatterns = [
    path('new/', NewBookingView.as_view(), name='new'),
    path('thank-you/', ThankYouView.as_view(), name='thank_you'),
]