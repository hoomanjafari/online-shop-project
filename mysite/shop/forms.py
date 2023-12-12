from django import forms


class ShopSortByForm(forms.Form):
    CHOICES = (
        ('added_time', 'جدیدترین ها'), ('-price', 'گرانترین ها'),
        ('-added_time',  'قدیمی ترین ها'), ('price', 'ارزان ترین ها')
    )
    sort_by = forms.ChoiceField(choices=CHOICES, label='')
