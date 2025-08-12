from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .models import Booking
from .forms import BookingForm


class NewBookingView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/new.html'
    success_url = reverse_lazy('bookings:thank_you')


class ThankYouView(TemplateView):
    template_name = 'bookings/thank_you.html'
