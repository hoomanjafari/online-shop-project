from django.contrib import admin
from .models import Shop, ShoingBag


class ShopAdmin(admin.ModelAdmin):
    list_filter = ('price', 'body')


admin.site.register(Shop, ShopAdmin)
admin.site.register(ShoingBag)
