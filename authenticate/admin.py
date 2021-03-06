from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib.auth.forms import UserChangeForm as DefaultUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DefaultUserCreationForm

from .models import User, UserStory, Category

class UserCreationFrom(DefaultUserCreationForm):
    class Meta(DefaultUserCreationForm.Meta):
        model = User


class UserChangeFrom(DefaultUserChangeForm):
    class Meta(DefaultUserChangeForm.Meta):
        model = User
        fields = DefaultUserChangeForm.Meta.fields


class UserAdmin(DefaultUserAdmin):
    model = User
    add_form = UserCreationFrom
    form = UserChangeFrom
    list_display = ["username", "is_active", "email", "role",'numberofus','rookie']
    exclude = (
        "groups",
        "is_staff",
    )

    add_user_info_fields = (
        "User info",
        {
            "fields": (
                "username",
                "email",
                "first_name",
                "profile_picture",
                "last_name",
                "password1",
                "password2",
            ),
        },
    )

    edit_user_info_fields = (
        "User info",
        {
            "fields": (
                "username",
                "email",
                "first_name",
                "role",
                "profile_picture",
                "last_name",
                "password",
            ),
        },
    )

    dates_fields = (
        "Dates",
        {
            "fields": (
                "date_joined",
                "last_login",
            )
        },
    )

    permission_fields = (
        "Permissions",
        {
            "fields": (
                "is_active",
                "is_superuser",
                "user_permissions",
            )
        },
    )

    edit_superuser_fields = (
        "Super user info",
        {
            "fields": (
                "username",
                "email",
                "password",
            ),
        },
    )

    add_fieldsets = (add_user_info_fields, dates_fields, permission_fields)
    fieldsets = (edit_user_info_fields, dates_fields, permission_fields)
    superuser_fieldset = (edit_superuser_fields, dates_fields, permission_fields)

    def get_fieldsets(self, request, user):
        if user is not None:
            if user.is_superuser:
                return self.superuser_fieldset
            else:
                return self.fieldsets
        else:
            return self.add_fieldsets



# Register your models here.

admin.site.register(UserStory)
admin.site.register(User, UserAdmin)
admin.site.register(Category)
