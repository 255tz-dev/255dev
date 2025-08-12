from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Destination, Activity


@admin.register(Activity)
class ActivityAdmin(TranslatableAdmin):
    list_display = ("__str__", "slug")
    search_fields = ("translations__name", "slug")


@admin.register(Destination)
class DestinationAdmin(TranslatableAdmin):
    list_display = ("__str__", "slug")
    search_fields = ("translations__name", "slug")
