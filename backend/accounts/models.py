from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class EmailUserManager(BaseUserManager):
    """
    A custom user manager to deal with email as unique identifier for auth
    instead of username.
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    # we always use a mail address to login, not an username
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True)

    # override username, as it is not used and therefor shouldn't be unique
    username = models.CharField(blank=True, max_length=255)

    REQUIRED_FIELDS = ('first_name', 'last_name')
    objects = EmailUserManager()
