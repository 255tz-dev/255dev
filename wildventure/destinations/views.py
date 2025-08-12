from django.views.generic import ListView, DetailView
from .models import Destination, Activity


class DestinationListView(ListView):
    model = Destination
    template_name = 'destinations/destination_list.html'
    context_object_name = 'destinations'


class DestinationDetailView(DetailView):
    model = Destination
    template_name = 'destinations/destination_detail.html'
    context_object_name = 'destination'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ActivityListView(ListView):
    model = Activity
    template_name = 'destinations/activity_list.html'
    context_object_name = 'activities'
