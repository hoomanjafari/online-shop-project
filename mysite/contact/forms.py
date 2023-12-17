from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        labels = {
            'name': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'number': 'شماره تماس'
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(ContactForm, self).__init__(*args, **kwargs)
