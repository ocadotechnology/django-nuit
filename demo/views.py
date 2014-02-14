from django.shortcuts import render
from nuit.views import PaginatedListView
from .models import Publisher

class MyListView(PaginatedListView):
    model = Publisher
    paginate_by = 15
    search_fields = ('name', ('address', 'iexact'))
