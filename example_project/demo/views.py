from django.shortcuts import render
from nuit.views import SearchableListView
from .models import Publisher
from .forms import PublisherForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

class MyListView(SearchableListView):
    model = Publisher
    template_name = 'demo/list_view.html'
    paginate_by = 15
    search_fields = ('name', ('address', 'iexact'))

def kitchen_sink(request):
    messages.set_level(request, messages.DEBUG)
    messages.add_message(request, messages.DEBUG, 'Debug Message')
    messages.add_message(request, messages.INFO, 'Info Message')
    messages.add_message(request, messages.SUCCESS, 'Success Message')
    messages.add_message(request, messages.WARNING, 'Warning Message')
    messages.add_message(request, messages.ERROR, 'Error Message')
    return render(request, 'demo/kitchensink.html', {})

def test_form(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = PublisherForm()
    return render(request, 'demo/forms.html', {'form': form})

def error(request, code='400'):
    return render(request, 'nuit/generic/%s.html' % code, {}, status=code)

@permission_required('does.not.exist')
def no_access(request):
    return 'Go Away'
