from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404


def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            if request.user.profile.userStatus in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return PermissionDenied
        return wrap
    return decorator


def customer_required(view_func):
    def wrap(request, *args, **kwargs):
        group = get_object_or_404(Group, name='Customer')
        if request.group == "Customer":
            return user_passes_test
        else:
            return PermissionDenied
    return wrap
