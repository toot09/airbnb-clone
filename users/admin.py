from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as rooms_models


class RoomInline(admin.TabularInline):
    model = rooms_models.Room


# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
@admin.register(models.User)
class CustomerUserAdmin(UserAdmin):

    """ Custom User Admin """

    # "UserAdmin.fieldsets" is provided function by Django
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profiles",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    # https://docs.djangoproject.com/en/2.2/ref/contrib/admin/
    # admin.site.register(models.User, CustomerUserAdmin)

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )

    inlines = (RoomInline,)
