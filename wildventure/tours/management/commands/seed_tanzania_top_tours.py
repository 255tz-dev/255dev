from django.core.management.base import BaseCommand
from tours.models import Category, Package
from decimal import Decimal
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Seed initial categories and top Tanzania tours'

    def handle(self, *args, **options):
        tanzania, _ = Category.objects.get_or_create(slug='tanzania-safaris')
        tanzania.set_current_language('en')
        tanzania.name = 'Tanzania Safaris'
        tanzania.description = 'Top Tanzania Tours'
        tanzania.save()

        zanzibar, _ = Category.objects.get_or_create(slug='zanzibar-safaris')
        zanzibar.set_current_language('en')
        zanzibar.name = 'Zanzibar Safaris'
        zanzibar.description = 'Zanzibar Beach Holidays'
        zanzibar.save()

        tours = [
            '2 Days Manyara & Ngorongoro',
            '3 Days Serengeti National Park',
            '3 Days Ngorongoro Crater',
            '3 Days Lake Manyara',
            '3 Days Wildlife Adventure',
            '4 Days Serengeti & Ngorongoro',
            '4 Days Wildlife Special',
            '5 Days Wildlife Escapade',
            '6 Days Tanzania Highlights',
            '7 Days Best of Tanzania',
        ]
        created = 0
        for name in tours:
            slug = slugify(name)
            pkg, was_created = Package.objects.get_or_create(slug=slug, defaults={
                'category': tanzania,
                'price_usd': Decimal('1500.00'),
                'days': int(name.split()[0]),
                'people_min': 1,
                'people_max': 6,
                'is_top_pick': True,
            })
            pkg.set_current_language('en')
            pkg.name = name
            pkg.summary = f"Summary of {name}"
            pkg.description = f"Detailed itinerary of {name}"
            pkg.highlights = f"Highlights of {name}"
            pkg.save()
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded {created} packages. Categories ensured."))