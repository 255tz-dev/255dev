from django.urls import path
from .views import DestinationListView, DestinationDetailView, ActivityListView

app_name = 'destinations'

urlpatterns = [
    path('', DestinationListView.as_view(), name='list'),
    path('experiences/', ActivityListView.as_view(), name='experiences'),
    path('<slug:slug>/', DestinationDetailView.as_view(), name='detail'),
]