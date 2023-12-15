from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from accounts.forms import UserLoginForm, UserRegisterForm
from django.contrib import messages
from .models import Shop, ShoingBag
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


class ShopItemDetail(View):
    def get(self, request, **kwargs):
        register_form = UserRegisterForm
        login_form = UserLoginForm
        item = get_object_or_404(Shop, pk=kwargs['pk'])
        return render(request, 'shop/shop_item_detail.html', {
            'item': item, 'register_form': register_form, 'login_form': login_form
        })


class AddItem(View):
    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            add_item = get_object_or_404(Shop, pk=kwargs['pk'])
            ShoingBag.objects.create(customer=request.user, item=add_item)
            messages.success(request, 'اضافه شد به سبد خریدتون', 'success')
            return redirect('shop:shop-shoes')
        else:
            add_item = get_object_or_404(Shop, pk=kwargs['pk'])
            messages.error(request, 'قبل از انتخاب محصول خود لطفا وارد حساب کاربریتون شوید', 'success')
            return redirect('shop:shoes_detail', add_item.id)


class CheckoutView(View):
    def get(self, request):
        register_form = UserRegisterForm
        login_form = UserLoginForm
        return render(request, 'shop/checkout.html', {'register_form': register_form, 'login_form': login_form})
