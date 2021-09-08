from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext as _


class ForgeNotification:
    subject = _('Welcome to Liip Forge')
    recipient = [settings.EMAIL_ADMIN]
    sender = settings.EMAIL_SENDER
    template = 'email/base.html'
    context = {}

    def send(self):
        msg = EmailMultiAlternatives(
            subject=self.get_subject(),
            body=self.get_plain_message(),
            from_email=self.get_sender(),
            to=self.get_recipient(),
        )
        msg.attach_alternative(self.get_html_message(), "text/html")
        msg.send()

    def get_subject(self):
        return self.subject

    def get_recipient(self):
        return list(self.recipient)

    def get_sender(self):
        return self.sender

    def get_template(self):
        return self.template

    def get_context(self):
        return self.context

    def get_html_message(self):
        return render_to_string(self.get_template(), self.get_context())

    def get_plain_message(self):
        return strip_tags(self.get_html_message())
