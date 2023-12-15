from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    image = models.ImageField(upload_to='img/%y')
    subject = models.CharField(max_length=12)
    body = models.CharField(max_length=17)
    price = models.FloatField(null=True, blank=True)
    shoes = models.BooleanField(default=False)
    bag = models.BooleanField(default=False)
    scarf = models.BooleanField(default=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self. subject} -- {self.body} -- {self.image}'


class ShoingBag(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer_related')
    item = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='item_related')

    def __str__(self):
        return f'{self.customer} -- want to buy : {self.item}'
