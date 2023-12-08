from django import forms


class UserRegisterForm(forms.Form):
    email = forms.EmailField(label='ایمیل ')
    password = forms.CharField(label='رمز ورود ')


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='ایمیل ')
    password = forms.CharField(label='رمز ورود ')
