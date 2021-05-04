
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, default=' ', null=True, blank=True)
    employee_cell_phone = models.CharField (max_length=50, default=' ', null=True, blank=True)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    class Meta:
        db_table = "employee"