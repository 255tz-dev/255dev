from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Offer(TranslatableModel):
    is_active = models.BooleanField(default=True)
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        url=models.URLField(blank=True, null=True),
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.safe_translation_getter('title', any_language=True) or "Offer"


class GlobalSettings(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return "Global Settings"
