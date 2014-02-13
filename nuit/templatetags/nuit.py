from django import template
import re

register = template.Library()

def is_quoted(string):
    return string[0] == string[-1] and string[0] in ('"', '"')

@register.simple_tag
def set_active_menu(active_menu):
    return "<span style='display: none' class='nuit-active-menu'>%s</span>" % active_menu


#@register.tag
def autoescape(parser, token):
    """
    Force autoescape behavior for this block.
    """
    args = token.contents.split()
    if len(args) != 2:
        raise TemplateSyntaxError("'autoescape' tag requires exactly one argument.")
    arg = args[1]
    if arg not in ('on', 'off'):
        raise TemplateSyntaxError("'autoescape' argument should be 'on' or 'off'")
    nodelist = parser.parse(('endautoescape',))
    parser.delete_first_token()
    return AutoEscapeControlNode((arg == 'on'), nodelist)

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
