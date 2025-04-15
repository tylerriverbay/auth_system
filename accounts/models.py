from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission

# Create your models here.
class CustomUser(AbstractUser):
    '''Extends django's AbstractUser to add a role field'''
    ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.ForeignKey('Role', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
    
class Role(models.Model):
    '''Model to store user roles'''
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.name