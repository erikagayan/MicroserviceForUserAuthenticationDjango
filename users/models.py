from django.db import models
from django.utils.translation import gettext
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    """User model"""

    # write any field
    is_moderator = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    email = models.EmailField(gettext("email address"), unique=True)
    username = models.CharField(gettext("username"), unique=True, max_length=150)

    # Email for auth
    USERNAME_FIELD = "email"
    # Required fields for creat superuser
    REQUIRED_FIELDS = ["username"]

    # For this model you should use the custom UserManager
    objects = UserManager()

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    class Meta:
        verbose_name = gettext("user")
        verbose_name_plural = gettext("users")
