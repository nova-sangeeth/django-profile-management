from django.conf.urls import url
from .views import employee_profile, employee_register


urlpatterns = [
    url(r'^employee_profile$', employee_profile, name="employee_profile"),
    url(r'^employee_register$', employee_register, name="employee_register"),
]
