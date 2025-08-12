from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.urls import reverse


class Activity(TranslatableModel):
    slug = models.SlugField(unique=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=150),
        description=models.TextField(blank=True),
    )

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or self.slug


class Destination(TranslatableModel):
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=150),
        how_to_get_there=models.TextField(blank=True),
        activities_text=models.TextField(blank=True),
    )
    activities = models.ManyToManyField(Activity, related_name='destinations', blank=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or self.slug

    def get_absolute_url(self):
        return reverse('destinations:detail', args=[self.slug])
