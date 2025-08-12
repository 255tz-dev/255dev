from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Offer, GlobalSettings


@admin.register(Offer)
class OfferAdmin(TranslatableAdmin):
    list_display = ("__str__", "is_active", "created_at")
    list_filter = ("is_active",)


@admin.register(GlobalSettings)
class GlobalSettingsAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "whatsapp")
