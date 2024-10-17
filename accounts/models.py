from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


# Create your models here.

class Customeruser(AbstractUser, PermissionsMixin):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        CUSTOMER = 'customer', 'Customer'
        TEACHER = 'teacher', 'Teacher'
        STUDENT = 'student', 'Student'
        GUEST = 'guest', 'Guest'
    
    base_role   = Role.ADMIN

    role        = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)  
