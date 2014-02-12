from django.shortcuts import render

def home(request):

    template_name = request.GET.get('template', 'bothmenu-topbar')

    return render(request, 'nuit/%s.html' % template_name, {'current_menu': template_name})

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
