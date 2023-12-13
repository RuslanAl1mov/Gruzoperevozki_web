from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import User, Gruz


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'father_name', 'company_name', 'is_staff'
        )

    fieldsets = (
        ('Personal info', {
            'fields': ('username', 'password', 'first_name', 'last_name', 'father_name', 'company_name', 'is_staff')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
             'fields': ('first_name', 'last_name', 'father_name', 'company_name', 'is_staff')
        }),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Gruz)

