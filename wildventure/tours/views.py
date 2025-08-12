from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Package, Category


class PackageListView(ListView):
    model = Package
    template_name = 'tours/package_list.html'
    context_object_name = 'packages'
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset().select_related('category')
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug')
        context['categories'] = Category.objects.all()
        context['active_category'] = None
        if category_slug:
            context['active_category'] = get_object_or_404(Category, slug=category_slug)
        return context


class PackageDetailView(DetailView):
    model = Package
    template_name = 'tours/package_detail.html'
    context_object_name = 'package'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return super().get_queryset().select_related('category').prefetch_related('itinerary_items')
