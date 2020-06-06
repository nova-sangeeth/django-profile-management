from allauth.account.adapter import DefaultAccountAdapter
from django.conf.urls import reverse


class AccountAdater(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return reverse('profile_management_app:index')

    def get_logout_redirect_url(self, request):
        return reverse('profile_management_app:index')
