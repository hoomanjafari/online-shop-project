from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(forms.Form):
    email = forms.EmailField(label='ایمیل ')
    password = forms.CharField(label='رمز ورود ', widget=forms.PasswordInput())

    def clean_email(self):
        form_email = self.cleaned_data['email']
        x = User.objects.filter(username=form_email)
        if x.exists():
            raise ValidationError('این ایمیل قبلا استفاده شده')
        else:
            return form_email


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='ایمیل ')
    password = forms.CharField(label='رمز ورود ', widget=forms.PasswordInput())


class ProfileEditForm(forms.ModelForm):
    new_password = forms.CharField(
        required=False, label=': رمز عبور جدید', label_suffix='*', widget=forms.PasswordInput()
    )
    new_password_confirm = forms.CharField(
        required=False, label=': تکرار رمز عبور جدید', label_suffix='*', widget=forms.PasswordInput()
    )

    def clean(self):
        cd = super().clean()
        # p1 = cd.get('password')
        p2 = cd.get('new_password')
        p3 = cd.get('new_password_confirm')
        if p2 and p3 and p2 != p3:
            raise ValidationError('رمز عبور جدید و تکرار رمز عبور جدید یکی نیستند')
        elif p2 != p3:
            raise ValidationError('رمز عبور جدید و تکرار رمز عبور جدید یکی نیستند1231')

    class Meta:
        model = Profile
        fields = ('name', 'phone_number')

        labels = {
            'name': ': نام و نام خانواد.',
            'phone_number': ': شماره تماس.',
        }
