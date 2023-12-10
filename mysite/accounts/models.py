from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_related')
    name = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} -- {self.name}'
