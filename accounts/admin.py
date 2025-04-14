from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Role

# Register your models here.
class CustomUserAdmin(UserAdmin):
    '''Custom admin configurations for CustomUser model'''
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {
            'fields': ('role',)}),
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role)