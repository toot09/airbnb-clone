from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    # OUTSIDE #

    list_display = (
        "name",
        "user",
        "count_rooms",
    )

    search_fields = (
        "^name",
        "^user__username",
    )

    # INSIDE #

    filter_horizontal = ("room",)
