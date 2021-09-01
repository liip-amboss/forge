from django.conf import settings


def notification(request):
    return {
        'EMAIL_BASE_URL': settings.EMAIL_BASE_URL
    }
