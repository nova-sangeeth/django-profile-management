from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


# Try the is staff decorator from django.contrib.admin.views.decorators import staff_member_required
# This decorator is not working and interupts the verification with usr groups.


def employee_group_required(*group_names):
    def in_group(user):
        if user.is_authenticated():
            if bool(u.groups.filter(name_in=group_names)) | user.is_superuser:
                return True
            raise PermissionDenied
        return False
    return user_passes_test(in_group)
