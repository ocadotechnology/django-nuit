from django.shortcuts import render
from nuit.views import SearchableListView
from .models import Publisher

class MyListView(SearchableListView):
    model = Publisher
    paginate_by = 15
    search_fields = ('name', ('address', 'iexact'))

# Form tests

from django.forms import ModelForm, ValidationError

class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'address', 'city', 'state_province', 'country', 'website',)
    def clean(self):
        raise ValidationError('Something went wrong')

def test_form(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = PublisherForm()
    return render(request, 'demo/publisher_form.html', {'form': form})
