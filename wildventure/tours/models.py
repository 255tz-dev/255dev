from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    slug = models.SlugField(unique=True)
    translations = TranslatedFields(
        name=models.CharField(max_length=150),
        description=models.TextField(blank=True),
    )

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['slug']

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or self.slug


class Package(TranslatableModel):
    category = models.ForeignKey(Category, related_name='packages', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    days = models.PositiveIntegerField(default=1)
    people_min = models.PositiveIntegerField(default=1)
    people_max = models.PositiveIntegerField(default=10)
    image = models.ImageField(upload_to='packages/', blank=True, null=True)
    is_top_pick = models.BooleanField(default=False)

    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        summary=models.TextField(blank=True),
        description=models.TextField(blank=True),
        highlights=models.TextField(blank=True),
    )

    class Meta:
        ordering = ['-is_top_pick', 'days', 'slug']

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or self.slug

    def get_absolute_url(self):
        return reverse('tours:package_detail', args=[self.slug])


class ItineraryItem(TranslatableModel):
    package = models.ForeignKey(Package, related_name='itinerary_items', on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='itineraries/', blank=True, null=True)

    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        description=models.TextField(),
    )

    class Meta:
        ordering = ['day_number']

    def __str__(self):
        base = self.safe_translation_getter('title', any_language=True) or f"Day {self.day_number}"
        return f"{self.package}: {base}"
