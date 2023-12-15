from django.shortcuts import render
from django.views import View
from accounts.forms import UserLoginForm, UserRegisterForm
from shop.models import ShoingBag


class HomeView(View):
    def get(self, request):
        register_form = UserRegisterForm
        login_form = UserLoginForm
        user_bag = ShoingBag.objects.filter(customer=request.user).count()
        return render(request, 'home/index.html', {
            'register_form': register_form, 'login_form': login_form, 'user_bag': user_bag
        })
