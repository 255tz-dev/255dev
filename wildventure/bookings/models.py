from django.db import models
from django.utils.translation import gettext_lazy as _
from destinations.models import Destination


class Booking(models.Model):
    class AccommodationChoice(models.TextChoices):
        BUDGET = 'budget', _('Budget')
        MID_RANGE = 'mid', _('Mid range')
        LUXURY = 'luxury', _('Luxury')

    class BudgetRange(models.TextChoices):
        RANGE_0_1000 = '0-1000', _('0-$1000')
        RANGE_1000_2000 = '1000-2000', _('1k - 2k')
        RANGE_2000_3000 = '2000-3000', _('2k - 3k')
        RANGE_4000_PLUS = '4000+', _('4k+')
        ANY = 'any', _("Budget doesn’t matter")

    prefix = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=150)
    country_of_residency = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp_number = models.CharField(max_length=50, blank=True)
    destination = models.ForeignKey(Destination, on_delete=models.SET_NULL, null=True, blank=True)
    number_of_days = models.PositiveIntegerField()
    number_of_people = models.PositiveIntegerField()
    travel_date = models.DateField()
    accommodation = models.CharField(max_length=10, choices=AccommodationChoice.choices)
    budget = models.CharField(max_length=20, choices=BudgetRange.choices)
    preferred_activities = models.TextField(blank=True)
    special_request = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Booking: {self.name} ({self.email})"
