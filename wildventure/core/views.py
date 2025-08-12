from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from bookings.forms import BookingForm
from tours.models import Package


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booking_form'] = BookingForm()
        context['top_packages'] = Package.objects.filter(is_top_pick=True)[:12]
        context['breadcrumbs'] = [("Home", "/")]  # minimal
        return context
