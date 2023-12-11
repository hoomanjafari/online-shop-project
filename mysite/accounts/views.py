from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, UserLoginForm, ProfileEditForm


class UserRegisterView(View):
    def post(self, request):
        form = UserRegisterForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username=cd['email'], password=cd['password'])
            messages.success(request, 'حساب کاربری شما ساخته شد', 'success')
            return redirect('home:home')
        else:
            messages.error(request, 'این ایمیل قبلا استفاده شده', 'danger')
            return redirect('home:home')


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
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'accounts/profile.html')


class AccountDetailView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home:home')
        else:
            return super().dispatch(request, *args, **kwargs)
            
    def get(self, request):
        profile_edit = ProfileEditForm(instance=request.user.profile_related)
        return render(request, 'accounts/profile-details.html', {
            'profile_edit': profile_edit
        })

    def post(self, request, **kwargs):
        form = ProfileEditForm(self.request.POST, instance=request.user.profile_related)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['new_password'] == '' and cd['new_password_confirm'] == '':
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                messages.success(request, 'تغییرات اعمال شدن', 'success')
                return redirect('accounts:account-detail')
            else:
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                user = get_object_or_404(User, pk=request.user.id)
                user.set_password(cd['new_password'])
                user.save()
                messages.success(request, 'تغییرات اعمال شدن و رمز عبور شما تغییر کرد لطفا دوباره وارد حساب کاربری خود شوید', 'success')
                return redirect('home:home')
        else:
            return render(request, 'accounts/profile-details.html', {'profile_edit': form})
