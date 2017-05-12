from django.db import models

from conduit.apps.core.models import TimestapedModel


class Profile(TimestapedModel):
    # One-to-one relationship between the two. Every user will have one -- and only
    # one -- related Profile model.
    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )

    bio = models.TextField(blank=True)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
