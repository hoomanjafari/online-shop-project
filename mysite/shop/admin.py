from django.contrib import admin
from .models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_filter = ('price', 'body')


admin.site.register(Shop, ShopAdmin)
