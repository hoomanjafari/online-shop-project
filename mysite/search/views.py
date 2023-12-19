from django.shortcuts import render
from django.views import View
from shop.models import Shop
from .forms import SearchForm
from accounts.forms import UserLoginForm, UserRegisterForm


class SearchView(View):
    def get(self, request):
        register_form = UserRegisterForm
        login_form = UserLoginForm
        search_result = ''
        if request.GET.get('search'):
            search_result = Shop.objects.filter(body__contains=request.GET['search'])
        return render(request, 'search/search-page.html', {
            'searched': search_result, 'search_form': SearchForm, 'register_form': register_form, 'login_form': login_form
        })
