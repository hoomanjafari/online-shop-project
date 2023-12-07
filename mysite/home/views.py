from django.shortcuts import render
from django.views import View
from accounts.forms import UserLoginForm, UserRegisterForm


class HomeView(View):
    def get(self, request):
        register_form = UserRegisterForm
        login_form = UserLoginForm
        return render(request, 'home/index.html', {
            'register_form': register_form, 'login_form': login_form
        })
