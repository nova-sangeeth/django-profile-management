from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class employee_profile(models.Model):
    gender_choices = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('others', 'others')
    )
    marital_choices = (
        ('Unmarried', 'Unmarried'),
        ('married', 'married'),
        ('others', 'others')
    )
    employee_position_choices = (
        ('manager', 'manager'),
        ('asst_manager', 'asst_manager'),
        ('cashier', 'cashier'),
        ('loan_approval', 'loan_approval')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=128, null=True)
    employee_position = models.CharField(
        max_length=128, null=True, choices=employee_position_choices)
    gender = models.CharField(
        max_length=128, choices=gender_choices, null=True)
    marital_status = models.CharField(
        max_length=128, choices=marital_choices, null=True)
    address = models.CharField(max_length=256, null=True)
    pincode = models.CharField(max_length=128, null=True)
    country = models.CharField(max_length=128, null=True, default='india')
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.name
