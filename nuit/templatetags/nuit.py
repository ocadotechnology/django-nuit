from django import template
from django.template.base import token_kwargs
from django.template.loader_tags import do_extends
from django.core.urlresolvers import reverse, NoReverseMatch
import re

register = template.Library()

def is_quoted(string):
    return string[0] == string[-1] and string[0] in ('"', '"')

@register.simple_tag
def set_active_menu(active_menu):
    '''
    Inserts a span with a class of .nuit-active-menu that is picked up by Javascript
    to highlight the correct menu item..
    '''
    return "<span style='display: none' class='nuit-active-menu'>%s</span>" % active_menu


class ExtendNode(template.Node):
    def __init__(self, node, kwargs):
        self.node = node
        self.kwargs = dict(("nuit_%s" % key, value) for key, value in kwargs.iteritems())

    def render(self, context):
        kwargs = dict((key, value.resolve(context)) for key, value in self.kwargs.iteritems())
        context.update(kwargs)
        try:
           return self.node.render(context)
        finally:
           context.pop()

@register.tag
def extend(parser, token):
    bits = token.split_contents()
    kwargs = token_kwargs(bits[2:], parser)
    token.contents = " ".join(bits[:2])

    # let the orginal do_extends parse the tag, and wrap the ExtendsNode
    return ExtendNode(do_extends(parser, token), kwargs)


class MenuSectionNode(template.Node):

    def __init__(self, nodelist, title=None, is_list=False, link_name=None):
        self.nodelist = nodelist
        self._title = title
        self.is_list = is_list
        self._link_name = link_name

    def get_link_name(self, context):
        if self.is_list:
            return ''
        if not self._link_name:
            return self.get_title(context)
        if is_quoted(self._link_name):
            return self._link_name[1:-1]
        try:
            return template.Variable(self._link_name).resolve(context)
        except template.VariableDoesNotExist:
            return ''

    def get_title(self, context):
        if not self._title:
            return ''
        if is_quoted(self._title):
            return self._title[1:-1]
        try:
            return template.Variable(self._title).resolve(context)
        except template.VariableDoesNotExist:
            return ''

    def render(self, context):
        content = self.nodelist.render(context)
        bare_title = self.get_title(context)
        title = '<h5>%s</h5>' % bare_title if bare_title else ''
        link_name = self.get_link_name(context)
        return '''
            <section data-link='{link_name}' data-id='{id}'>
                <div>
                {title}
                {list_begin}
                {content}
                {list_end}
                </div>
                <hr />
            </section>
        '''.format(
            title = title,
            content = content,
            link_name = link_name,
            id = re.sub(r'[^A-Za-z0-9]+', '', link_name),
            list_begin = "<nav><ul class='side-nav'>" if self.is_list else '',
            list_end = '</ul></nav>' if self.is_list else '',
        )


@register.tag
def menu_section(parser, token):
    '''
    Renders the correct HTML for a menu section.
    '''
    args = token.split_contents()
    kwargs = {}
    for kwarg in args[1:]:
        if '=' not in kwarg:
            kwargs['title'] = kwarg
            continue
        before, after = kwarg.split('=')
        kwargs[before] = after
    nodelist = parser.parse(('end_menu_section',))
    parser.delete_first_token()
    return MenuSectionNode(nodelist, **kwargs)


class AppMenuNode(template.Node):
    def __init__(self, nodelist, title=None):
        self.nodelist = nodelist
        self.title = title
    def render(self, context):
        content = self.nodelist.render(context)
        title = '<h5>%s</h5>' % self.title.resolve(context) if self.title else ''
        return "<section class='main-nav'>{title}<nav><ul class='side-nav'>{content}</ul></nav><hr /></section>".format(title=title, content=content)

@register.tag
def app_menu(parser, token):
    bits = token.split_contents()
    if len(bits) > 2:
        raise template.TemplateSyntaxError('Wrong number of arguments for app_menu - expected 2 maximum')
    title = None
    if len(bits) == 2:
        title = parser.compile_filter(bits[1])
    nodelist = parser.parse(('end_app_menu',))
    parser.delete_first_token()
    return AppMenuNode(nodelist, title=title)

@register.simple_tag
def menu_item(link, name, id):
    # try reversing the link to see if it is a view
    try:
        url = reverse(link)
    except NoReverseMatch:
        url = link
    return "<li class='menu-{id}'><a href='{link}'>{name}</a></li>".format(name=name, link=url, id=id)


@register.inclusion_tag('nuit/includes/_pagination_menu.html', takes_context=True)
def pagination_menu(context, page_obj, show_totals=True):
    total_pages = page_obj.paginator.page_range
    actual_numbers = [page for page in total_pages if page >= total_pages[-1] - 1 or page <= 2 or (page >= page_obj.number - 2 and page <= page_obj.number + 2)]
    page_list = []
    for i, number in enumerate(actual_numbers[:-1]):
        page_list.append(number)
        if actual_numbers[i + 1] != number + 1:
            page_list.append(None)
    page_list.append(actual_numbers[-1])
    return {
        'context': context,
        'page_obj': page_obj,
        'page_list': page_list,
        'show_totals': show_totals,
    }
