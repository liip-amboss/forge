from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import resolve_url
from django.urls import reverse
from django.utils.http import is_safe_url
from two_factor.admin import AdminSiteOTPRequired, AdminSiteOTPRequiredMixin


class AdminSiteOTPRequiredMixinRedirSetup(AdminSiteOTPRequired):
    def login(self, request, extra_context=None):
        redirect_to = request.POST.get(
            REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME)
        )
        if super(AdminSiteOTPRequiredMixin, self).has_permission(request):
            if request.user.is_verified():
                # already logged-in and verified by OTP
                index_path = reverse('admin:index', current_app=self.name)
            else:
                # user has permission but no OTP set:
                index_path = reverse('two_factor:setup', current_app=self.name)
            return HttpResponseRedirect(index_path)

        if not redirect_to or not is_safe_url(
            url=redirect_to, allowed_hosts=[request.get_host()]
        ):
            redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

        return redirect_to_login(redirect_to)
