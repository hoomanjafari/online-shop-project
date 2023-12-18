from django.shortcuts import render
from django.views import View
from shop.models import Shop
from .forms import SearchForm


class SearchView(View):
    def get(self, request):
        search_result = ''
        if request.GET.get('search'):
            search_result = Shop.objects.filter(body__contains=request.GET['search'])
        return render(request, 'search/search-page.html', {'searched': search_result, 'search_form': SearchForm})
