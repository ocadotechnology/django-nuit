import django
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.views.generic import DetailView


@staff_member_required
def view_needing_staff(request):
    # If this line is reached, the test as failed, as the
    # view visibility code should not execute views
    raise Exception  # pragma: no cover


@permission_required('auth.add_user')
def view_needing_add_user(request):
    # If this line is reached, the test as failed, as the
    # view visibility code should not execute views
    raise Exception  # pragma: no cover


class ViewNeedingAddUser(DetailView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('auth.add_user'):
            return super(ViewNeedingAddUser, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get(self, *_args, **_kwargs):
        # If this line is reached, the test as failed, as the
        # view visibility code should not execute views
        raise Exception  # pragma: no cover

if django.VERSION >= (1, 9, 0):
    from django.contrib.auth.mixins import PermissionRequiredMixin

    class MixinViewNeedingAddUser(PermissionRequiredMixin, DetailView):
        permission_required = 'auth.add_user'
        raise_exception = True

        def get(self, *_args, **_kwargs):
            # If this line is reached, the test as failed, as the
            # view visibility code should not execute views
            raise Exception  # pragma: no cover
