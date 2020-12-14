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
from django.conf.urls.static import static
from django.urls import include, re_path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('api/v1/account/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^.*', RedirectView.as_view(url='/admin/'), name='admin-redirect')
]

if settings.DEBUG:
    urlpatterns = (
        [
            path('api-auth/', include('rest_framework.urls',
                                      namespace='rest_framework')),
        ]
        + urlpatterns
    )
