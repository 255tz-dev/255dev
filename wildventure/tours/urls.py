from django.urls import path
from .views import PackageListView, PackageDetailView

app_name = 'tours'

urlpatterns = [
    path('', PackageListView.as_view(), name='package_list'),
    path('category/<slug:category_slug>/', PackageListView.as_view(), name='package_by_category'),
    path('<slug:slug>/', PackageDetailView.as_view(), name='package_detail'),
]