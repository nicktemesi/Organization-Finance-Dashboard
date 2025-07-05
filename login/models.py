from django.contrib.auth.models import AbstractUser
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('company_accountant', 'Company Accountant'),
        ('department_accountant', 'Department Accountant'),
        ('department_manager', 'Department Manager'),
    ]

    role = models.CharField(max_length=30, choices=ROLE_CHOICES)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Only used for Department Managers"
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
