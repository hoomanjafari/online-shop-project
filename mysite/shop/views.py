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
        user_bag = ''
        if request.user.is_authenticated:
            user_bag = ShoingBag.objects.filter(customer=request.user).count()
        if request.GET.get('sort_by'):
            shoes = Shop.objects.all().filter(shoes=True).order_by(request.GET['sort_by'])
        return render(request, 'shop/shop_shoes.html', {
            'register_form': register_form, 'login_form': login_form, 'shoes': shoes, 'shop_select': shop_select,
            'user_bag': user_bag
        })


class ShopItemDetail(View):
    def get(self, request, **kwargs):
        register_form = UserRegisterForm
        login_form = UserLoginForm
        user_bag = ShoingBag.objects.filter(customer=request.user).count()
        item = get_object_or_404(Shop, pk=kwargs['pk'])
        return render(request, 'shop/shop_item_detail.html', {
            'item': item, 'register_form': register_form, 'login_form': login_form, 'user_bag': user_bag
        })


class AddItem(View):
    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            add_item = get_object_or_404(Shop, pk=kwargs['pk'])
            already_added = ShoingBag.objects.filter(customer=request.user)
            if not already_added:
                ShoingBag.objects.create(customer=request.user, item=add_item)
                messages.success(request, 'اضافه شد به سبد خریدتون', 'success')
                return redirect('shop:shop-shoes')
            else:
                messages.error(request, 'این محصول قبلا اضافه شده به سبد خرید شما', 'danger')
                return redirect('shop:shoes_detail', add_item.id)
        else:
            add_item = get_object_or_404(Shop, pk=kwargs['pk'])
            messages.error(request, 'قبل از انتخاب محصول خود لطفا وارد حساب کاربریتون شوید', 'success')
            return redirect('shop:shoes_detail', add_item.id)


class DeleteItem(View):
    def get(self, request, **kwargs):
        item = get_object_or_404(ShoingBag, pk=kwargs['pk'])
        if request.user.is_authenticated:
            item.delete()
            messages.success(request, 'کالا از سبذ خرید شما حذف شد', 'success')
            return redirect('shop:checkout')
        else:
            return redirect('home:home')


class CheckoutView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        register_form = UserRegisterForm
        login_form = UserLoginForm
        user_bag = ShoingBag.objects.filter(customer=request.user).count()
        cart_item = ShoingBag.objects.filter(customer=request.user)
        total_price = 0
        for i in cart_item:
            total_price += i.item.price
        return render(request, 'shop/checkout.html', {
            'register_form': register_form, 'login_form': login_form, 'total_price': total_price, 'cart_item': cart_item,
            'user_bag': user_bag
        })
