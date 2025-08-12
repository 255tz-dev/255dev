from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableStackedInline
from .models import Category, Package, ItineraryItem


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ("__str__", "slug")


class ItineraryInline(TranslatableStackedInline):
    model = ItineraryItem
    extra = 1


@admin.register(Package)
class PackageAdmin(TranslatableAdmin):
    list_display = ("__str__", "category", "price_usd", "days", "is_top_pick")
    list_filter = ("category", "is_top_pick")
    search_fields = ("translations__name", "slug")
    inlines = [ItineraryInline]


@admin.register(ItineraryItem)
class ItineraryItemAdmin(TranslatableAdmin):
    list_display = ("package", "day_number", "__str__")
    list_filter = ("package",)
