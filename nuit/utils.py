'''Utils.'''

from django.core.exceptions import PermissionDenied

def get_callable_cells(function):
    '''
    Iterate through all of the decorators on this function,
    and put those that might be callable onto our callable stack.
    '''
    callables = []
    if not hasattr(function, 'func_closure'):
        if hasattr(function, 'view_func'):
            return get_callable_cells(function.view_func)
    if not function.func_closure:
        return [function]
    for closure in function.func_closure:
        if hasattr(closure.cell_contents, '__call__'):
            # Class-based view does not have a .func_closure attribute.
            # Instead, we want to look for decorators on the dispatch method.
            # We can also look for decorators on a "get" method, if one exists.
            if hasattr(closure.cell_contents, 'dispatch'):
                callables.extend(get_callable_cells(closure.cell_contents.dispatch.__func__))
                if hasattr(closure.cell_contents, 'get'):
                    callables.extend(get_callable_cells(closure.cell_contents.get.__func__))
            elif hasattr(closure.cell_contents, 'func_closure') and closure.cell_contents.func_closure:
                callables.extend(get_callable_cells(closure.cell_contents))
            else:
                callables.append(closure.cell_contents)
    return [function] + callables

def get_user_tests(function):
    '''
    Get a list of callable cells attached to this function that have the first
    parameter named "u" or "user".
    '''
    return [
        x for x in get_callable_cells(function)
        if getattr(x, 'func_code', None) and (
            x.func_code.co_varnames[0] in ["user", "u"] or
            (len(x.func_code.co_varnames) > 1 and x.func_code.co_varnames[0] in ['self', 'cls'] and x.func_code.co_varnames[1] in ['u', 'user'])
        )
    ]

def test_view(test, urlconf, user):
    '''
    Run a view test. Add in *args, **kwargs if appropriate.
    '''
    args = [] if 'args' not in test.func_code.co_varnames else urlconf.args
    kwargs = {} if 'kwargs' not in test.func_code.co_varnames else urlconf.kwargs
    return test(user, *args, **kwargs)

def user_can_see_view(view, user):
    '''
    Can the user see this view?
    '''
    try:
        can_view = all([test_view(test, view, user) for test in get_user_tests(view.func)])
    except PermissionDenied:
        return False

    return can_view
