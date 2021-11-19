from django.core.mail import send_mail

from accounts.tokens import token_generator
from django.conf import settings


def send_initial_email(to, token):
    send_mail(
        'Password Reset',
        f'https://{settings.FRONTEND_URL}/password-reset?token={token}',
        settings.EMAIL_SENDER,
        [to],
        fail_silently=False,
    )


def check_token(user, token):
    if not user:
        return False

    return token_generator.check_token(user, token)
