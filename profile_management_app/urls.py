from django.conf.urls import url
from .views import index, profile, registration, edit_profile


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^profile$', profile, name="profile"),
    url(r'^edit_profile$', edit_profile, name="edit_profile"),
    url(r'^registration$', registration, name="registration"),
]
