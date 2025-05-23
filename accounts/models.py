from datetime import date
from django.conf import settings
from django.conf import settings  # This references your custom user model
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=255)

    REQUIRED_FIELDS = ['email']


class UserChances(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_chances'
    )
    # Default total chances (modifiable later)
    total_chances = models.IntegerField(default=10)
    # Initially set to total chances
    chances_left = models.IntegerField(default=10)
    updated_at = models.DateTimeField(auto_now=True)  # To track updates
    last_reset_date = models.DateField(
        auto_now_add=True)  # Tracks the last reset date

    def __str__(self):
        return f"{self.user.username} - Total Chances: {self.total_chances}, Left: {self.chances_left}"

    def reduce_chances(self):
        """
        Reduces the chances_left by 1 if greater than 0.
        Resets chances if the day has changed.
        """
        # Check if the day has changed
        if self.last_reset_date != date.today():
            self.reset_chances()

        # Reduce chances if available
        if self.chances_left > 0:
            self.chances_left -= 1
            self.save()

    def reset_chances(self):
        """
        Resets chances_left to total_chances and updates last_reset_date.
        """
        self.chances_left = self.total_chances
        self.last_reset_date = date.today()
        self.save()
