from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Department


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # This controls what is shown on the user list page
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'department', 'is_staff')

    # These fields will be shown when editing/creating a user
    fieldsets = UserAdmin.fieldsets + (
        ('Role & Department', {
            'fields': ('role', 'department'),
        }),
    )

    # These fields will appear when creating a user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role & Department', {
            'fields': ('role', 'department'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department)
