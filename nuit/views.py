from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

class PaginatedListView(ListView):
    object_link = True
    search_fields = ()

    def get_context_data(self, **kwargs):
        context = super(PaginatedListView, self).get_context_data(**kwargs)
        if self.search_fields:
            context['search'] = True
            q = self.request.GET.get('q')
            if q:
                context['search_query'] = q
        context['object_link'] = self.object_link
        return context

    def get_queryset(self):
        queryset = super(PaginatedListView, self).get_queryset()
        if self.search_fields:
            q = self.request.GET.get('q')
            if q is None:
                return queryset
            # TODO: do the actual search
            queryset = self.search_queryset(queryset, q)
        return queryset

    def search_queryset(self, queryset, search_term):
        query = Q()
        for field in self.search_fields:
            lookup = 'icontains'
            if not isinstance(field, basestring):
                field, lookup = field
            query = query | Q(**{'%s__%s' % (field, lookup): search_term})
        print query
        return queryset.filter(query)











#===================================================

def home(request):

    template_name = request.GET.get('template', 'bothmenu-topbar')

    return render(request, 'nuit/mytemplate.html', {'template_name': 'nuit/%s.html' % template_name, 'template_short_name': template_name})

def app_menu(request):
    return (
        {
            'id': 'empty',
            'name': 'Empty',
            'link': '?template=empty',
        },
        {
            'id': 'topbar',
            'name': 'Top Bar',
            'link': '?template=topbar',
        },
        {
            'id': 'leftmenu',
            'name': 'Left Menu',
            'link': '?template=leftmenu',
        },
        {
            'id': 'rightmenu',
            'name': 'Right Menu',
            'link': '?template=rightmenu',
        },
        {
            'id': 'bothmenu',
            'name': 'Both Menus',
            'link': '?template=bothmenu',
        },
        {
            'id': 'leftmenu-topbar',
            'name': 'Left Menu & Top Bar',
            'link': '?template=leftmenu-topbar',
        },
        {
            'id': 'rightmenu-topbar',
            'name': 'Right Menu & Top Bar',
            'link': '?template=rightmenu-topbar',
        },
        {
            'id': 'bothmenu-topbar',
            'name': 'Both Menus & Top Bar',
            'link': '?template=bothmenu-topbar',
        },
    )
