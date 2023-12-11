from django.shortcuts import render
from django.views import View
from accounts.forms import UserLoginForm, UserRegisterForm
from .models import Shop


class ShopView(View):
    def get(self, request):
        register_form = UserRegisterForm
        login_form = UserLoginForm
        shoes_p = Shop.objects.all().filter(shoes=True).order_by('price')
        shoes_t = Shop.objects.all().filter(shoes=True).order_by('added_time')
        return render(request, 'shop/shop_shoes.html', {
            'register_form': register_form, 'login_form': login_form, 'shoes_p': shoes_p, 'shoes_t': shoes_t
        })
