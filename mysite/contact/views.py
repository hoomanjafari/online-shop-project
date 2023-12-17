from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from shop.models import ShoingBag
from .forms import ContactForm
from accounts.forms import UserLoginForm, UserRegisterForm


class ContactView(View):
    def get(self, request):
        login_form = UserLoginForm
        register_form = UserRegisterForm
        user_bag = ''
        if request.user.is_authenticated:
            user_bag = ShoingBag.objects.filter(customer=request.user).count()
        return render(request, 'contact/contact.html', {
            'user_bag': user_bag, 'form': ContactForm, 'login_form': login_form, 'register_form': register_form
        })

    def post(self, request):
        form = ContactForm(self.request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات شما ذخیره شد', 'success')
            return redirect('contact:contact')
        else:
            return render(request, 'contact/contact.html', {'form': form})
