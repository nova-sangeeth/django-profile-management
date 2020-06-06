from django.shortcuts import render, get_object_or_404, redirect
from .models import employee_profile
from .forms import employee_profile_form
from .decorators import employee_group_required
from django.contrib.auth.models import User, Group


def employee_profile(reqeust):
    return render(reqeust, 'employee_profile.html')


def employee_register(request):
    user = User.objects.get(username=request.user.username)
    group = Group.objects.get(name='Employee')
    employee = employee_profile(user=user)
    form = employee_profile_form(request.POST or None, instance=employee)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            group = get_object_or_404(Group, name='Employee')
            user.groups.add(group)
            print('----------------------------')
            print('Added', user, ' to Employee group')
            print('----------------------------')
            print(group, user)
            return redirect('profile')

    return render(request, "employee_register.html", {"form": form, "group": group})


def employee_profile_edit(request):
    pass
