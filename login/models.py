from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo_url = models.URLField()

    def __str__(self):
        return self.user.username
