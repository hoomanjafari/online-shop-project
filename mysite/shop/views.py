from django.shortcuts import render
from django.views import View
from accounts.forms import UserLoginForm, UserRegisterForm
from .models import Shop
from .forms import ShopSortByForm


class ShopView(View):
    def get(self, request):
        shop_select = ShopSortByForm
        register_form = UserRegisterForm
        login_form = UserLoginForm
        shoes = Shop.objects.all().filter(shoes=True)
        if request.GET.get('sort_by'):
            shoes = Shop.objects.all().filter(shoes=True).order_by(request.GET['sort_by'])
        return render(request, 'shop/shop_shoes.html', {
            'register_form': register_form, 'login_form': login_form, 'shoes': shoes, 'shop_select': shop_select,
        })
