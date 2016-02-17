from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.views.generic import DetailView


@staff_member_required
def view_needing_staff(request):
    raise Exception


@permission_required('auth.add_user')
def view_needing_add_user(request):
    raise Exception


class ViewNeedingAddUser(DetailView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('auth.add_user'):
            return super(ViewNeedingAddUser, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get(self, *_args, **_kwargs):
        raise Exception
