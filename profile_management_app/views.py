from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from .form import customer_profile_form
from .models import customer_profile
from django.contrib.auth.decorators import login_required
from .decorators import customer_required


def index(request):
    return render(request, "index.html")


def registration(request):
    user = User.objects.get(username=request.user.username)
    # group = Group.objects.get(name='Customer')
    customer = customer_profile(user=user)
    customer_status = customer_profile()
    form = customer_profile_form(request.POST or None, instance=customer)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            # group = get_object_or_404(Group, name='Customer')
            # user.groups.add(group)
            # print('----------------------------')
            # print('Added', user, ' to Customer group')
            # print('----------------------------')
            # print(group, user)
            return redirect('profile')

    return render(request, "registeration.html", {"form": form, "customer_status": customer_status})

# The decorator user to separate the user from different groups.
# @customer_required


@login_required
def profile(request):
    user = customer_profile.objects.filter(user=request.user)
    return render(request, "profile.html", {"data": user})


@login_required
def edit_profile(request):
    user = get_object_or_404(User, username=request.user.username)
    customer = get_object_or_404(customer_profile, user=user)
    form = customer_profile_form(
        request.POST or None, instance=customer)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("profile")

    return render(request, "edit_profile.html", {'form': form})
