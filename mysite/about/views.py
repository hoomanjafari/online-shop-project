from django.shortcuts import render
from django.views import View
from accounts.forms import UserRegisterForm, UserLoginForm
from shop.models import ShoingBag


class AboutUsView(View):
    def get(self, request):
        register_form = UserRegisterForm
        login_form = UserLoginForm
        user_bag = ''
        if request.user.is_authenticated:
            user_bag = ShoingBag.objects.filter(customer=request.user).count()
        return render(request, 'about/abou-us.html', {
            'register_form': register_form, 'login_form': login_form, 'user_bag': user_bag
        })
