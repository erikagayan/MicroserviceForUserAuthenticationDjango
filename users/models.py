from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    """Custom user model"""

    # Write your custom fields
    is_moderator = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    # Redefined email
    email = models.EmailField(unique=True)

    # Email for auth
    USERNAME_FIELD = "email"
    # Required fields for creat superuser
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    # If we create user in admin panel, normalize email
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
