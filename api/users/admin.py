from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email',)
    list_filter = ('email', 'is_active', 'is_staff', 'is_vendor',)
    ordering = ('-start_date',)
    list_display = ('email',
                    'is_active', 'is_staff', 'is_vendor',)
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_vendor',)}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)
