from django import forms
from .models import Profile

class UserRegisterForm(forms.Form):
    email = forms.EmailField(label='ایمیل ')
    password = forms.CharField(label='رمز ورود ')


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='ایمیل ')
    password = forms.CharField(label='رمز ورود ')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'phone_number')

        labels = {
            'name': ': نام و نام خانواد.',
            'phone_number': ': شماره تماس.',
        }


class ProfilePasswordEditForm(forms.Form):
    password = forms.CharField(label=': رمز عبور کنونی', label_suffix='*', widget=forms.PasswordInput(attrs={
        'autocomplete': 'off'
    }))
    new_password = forms.CharField(label=': رمز عبور جدید', label_suffix='*', widget=forms.PasswordInput())
