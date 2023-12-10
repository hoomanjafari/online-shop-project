from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, UserLoginForm, ProfileEditForm, ProfilePasswordEditForm



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


class AccountDetailView(View):
    def get(self, request):
        profile_edit = ProfileEditForm(instance=request.user.profile_related)
        profile_password = ProfilePasswordEditForm
        return render(request, 'accounts/profile-details.html', {
            'profile_edit': profile_edit, 'profile_password': profile_password
        })

    def post(self, request):
        form = ProfileEditForm(self.request.POST, instance=request.user.profile_related)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'تغییرات اعمال شدن', 'success')
            return redirect('accounts:account-detail')
        else:
            return render(request, 'accounts/profile-details.html', {'profile_edit': form})


# class AccountPasswordView(View):
#     def post(self, request):
#         form = ProfilePasswordEditForm(self.request.POST)
#         if form.is_valid():
            