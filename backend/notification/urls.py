from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

from notification.views import BaseEmail, TestEmail

urlpatterns = [
    path('template', staff_member_required(BaseEmail.as_view()), name='template'),
    path('test', staff_member_required(TestEmail.as_view()), name='test'),
]
