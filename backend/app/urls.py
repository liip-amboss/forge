"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


auth_urls = []
if not settings.DISABLE_2FA:
    from two_factor.urls import urlpatterns as tf_urls
    from accounts.two_factor import AdminSiteOTPRequiredMixinRedirSetup

    admin.site.__class__ = AdminSiteOTPRequiredMixinRedirSetup
    auth_urls = [path('', include(tf_urls))]

api_url_patterns = [
    path('api/v1/account/', include('accounts.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title='Forge API',
        default_version='0.0.1',
        description='This document contains the api documentation for the '
        'Forge project. <br /><br />',
    ),
    patterns=api_url_patterns,
    public=True,
)

urlpatterns = (
    auth_urls
    + api_url_patterns
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + [
        path('admin/', admin.site.urls),
    ]
)

# Only add redoc if redoc is enabled
if settings.ENABLE_REDOC:
    urlpatterns = [
        url(r'^redoc/$', schema_view.with_ui('redoc'), name='schema-redoc'),
    ] + urlpatterns

if settings.DEBUG:
    urlpatterns = [
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        path('notification/', include('notification.urls')),
    ] + urlpatterns
