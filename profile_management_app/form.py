from django.forms import ModelForm
from .models import customer_profile


class customer_profile_form(ModelForm):
    class Meta:
        model = customer_profile
        fields = '__all__'
        exclude = ('user',)
