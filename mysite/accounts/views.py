from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, UserLoginForm


class UserRegisterView(View):
    def post(self, request):
        form = UserRegisterForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['email'], password=cd['password'])
            return redirect('home:home')
        else:
            return render(request, 'home/index.html', UserRegisterForm())


class UserLoginView(View):
    def post(self, request):
        form = UserLoginForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home:home')
            elif user is None:
                messages.error(request, 'ایمیل یا رمز عبور اشتباه است', 'danger')
                return redirect('home:home')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home:home')


class AccountView(View):
    def get(self, request):
        return render(request, 'accounts/profile.html')
