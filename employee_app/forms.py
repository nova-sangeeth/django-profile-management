from django.forms import ModelForm
from .models import employee_profile


class employee_profile_form(ModelForm):
    class Meta:
        model = employee_profile
        fields = '__all__'
        exclude = ('user',)
