from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View

from notification.mail import ForgeNotification


class BaseEmail(TemplateView):
    template_name = 'email/base.html'


class TestEmail(View):
    def get(self, request, *args, **kwargs):
        email = request.GET.get('email', None)
        if not email:
            return HttpResponse('Please pass your email address with the `email` get param!')

        message = ForgeNotification()
        message.sender = 'be-dev@liip.ch'
        message.recipient = [email,]
        message.subject = 'Forge Test Email'
        message.send()

        return HttpResponse(f'Email has been sent to {email}')
