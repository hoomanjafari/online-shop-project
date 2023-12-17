from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=33)
    email = models.EmailField()
    number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} -- {self.number}'
