from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from accounts.forms import UserLoginForm, UserRegisterForm
from shop.models import ShoingBag
from .forms import HomeContactForm


class HomeView(View):
    def get(self, request):
        register_form = UserRegisterForm
        login_form = UserLoginForm
        user_bag = ''
        if request.user.is_authenticated:
            user_bag = ShoingBag.objects.filter(customer=request.user).count()
        return render(request, 'home/index.html', {
            'register_form': register_form, 'login_form': login_form, 'user_bag': user_bag, 'form': HomeContactForm
        })


class HomeContactView(View):
    def post(self, request):
        form = HomeContactForm(self.request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات شما ذخیره شد', 'success')
            return redirect('home:home')
        else:
            return render(request, 'home/index.html', {'form': form})
