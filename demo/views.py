from django.shortcuts import render
from nuit.views import SearchableListView
from .models import Publisher

class MyListView(SearchableListView):
    model = Publisher
    paginate_by = 15
    search_fields = ('name', ('address', 'iexact'))
