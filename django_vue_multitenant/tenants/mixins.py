from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.shortcuts import get_object_or_404, redirect

class UserPermissionMixin(object):

    def dispatch(self, request,*args, **kwargs):
        group = request.user.groups.filter(user=request.user)[0]
        
        if group.name=="client":
            return redirect('clients:clientlandingpage')

        return super(UserPermissionMixin, self).dispatch(request, *args, **kwargs)