from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User

    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_active')
    search_fields = ['first_name', 'last_name', 'email']
    add_fieldsets = (
        ('Account', {
            'fields': ('email', 'password1', 'password2',)
        }),
    )
    fieldsets = (
        ('Account', {
            'fields': ('email', 'password', 'first_name', 'last_name')
        }),
        ('Intern', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )
