from .models import GlobalSettings, Offer


def global_settings(request):
    settings_obj = GlobalSettings.objects.first()
    offers = Offer.objects.filter(is_active=True)[:5]
    return {
        'global_settings': settings_obj,
        'active_offers': offers,
    }