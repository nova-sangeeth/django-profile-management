from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class customer_profile(models.Model):

    gender_choices = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('others', 'others')
    )
    marital_choices = (
        ('Unmarried', 'Unmarried'),
        ('married', 'married'),
        ('none', 'none')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=128, null=True)
    gender = models.CharField(
        max_length=128, choices=gender_choices, null=True)
    marital_status = models.CharField(
        max_length=128, choices=marital_choices, null=True)
    address = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=14, null=True)
    email = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name
