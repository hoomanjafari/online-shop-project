from django.db import models


class Shop(models.Model):
    image = models.ImageField(upload_to='img/%y')
    subject = models.CharField(max_length=12)
    body = models.CharField(max_length=17)
    price = models.CharField(max_length=17)
    shoes = models.BooleanField(default=False)
    bag = models.BooleanField(default=False)
    scarf = models.BooleanField(default=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self. subject} -- {self.body}'
