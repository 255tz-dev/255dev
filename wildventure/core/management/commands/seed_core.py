from django.core.management.base import BaseCommand
from core.models import GlobalSettings, Offer


class Command(BaseCommand):
    help = 'Seed core data like global settings and sample offers'

    def handle(self, *args, **options):
        if not GlobalSettings.objects.exists():
            GlobalSettings.objects.create(
                email='info@wildventure.tz',
                phone='+255 700 000 000',
                whatsapp='+255700000000',
                address='Arusha, Tanzania'
            )
            self.stdout.write(self.style.SUCCESS('Created GlobalSettings'))
        else:
            self.stdout.write('GlobalSettings already exist')

        if not Offer.objects.exists():
            offer = Offer.objects.create(is_active=True)
            offer.set_current_language('en')
            offer.title = 'Early Bird Offer'
            offer.url = '#'
            offer.save()
            self.stdout.write(self.style.SUCCESS('Created sample Offer'))
        else:
            self.stdout.write('Offers already exist')