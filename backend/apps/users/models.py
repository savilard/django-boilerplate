from django.contrib.auth.models import AbstractUser

from apps.core.models import TimestampedModel


class CustomUser(AbstractUser, TimestampedModel):
    """Custom user model."""

    pass

    def __str__(self):
        return self.username
