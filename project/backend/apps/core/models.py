import uuid

from django.db import models

from behaviors.behaviors import Timestamped


class DefaultModel(models.Model):
    """Project default model."""

    uuid = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimestampedModel(DefaultModel, Timestamped):
    """
    Default app model that has `created` and `updated` attributes.

    Currently based on https://github.com/audiolion/django-behaviors
    """

    class Meta:
        abstract = True
