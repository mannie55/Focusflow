from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    focus_duration = models.PositiveIntegerField(default=25)
    habit_type = models.CharField(max_length=100, blank=True)
    is_google_user = models.BooleanField(default=False)
    # Optional: later, we can add profile picture, bio, streak, etc.

    def __str__(self):
        return self.username
