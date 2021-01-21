from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Deffinition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        # All Items has related_name "rooms"
        return obj.rooms.count()


# InlineModelAdmin
class PhotoInline(admin.TabularInline):
    model = models.Photo


# Register your models here.
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Deffinition """

    # @@@@@ [OUTSIDE Expression] @@@@@ #

    """ List in Admin Penal """
    list_display = (
        "name",
        "country",
        "city",
        "address",
        "prices",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("city", "prices")

    """ [Filter] """
    list_filter = (
        "instant_book",
        "host__gender",
        "host__superhost",
        "room_type",
        "amenity",
        "facility",
        "house_rules",
        "city",
        "country",
    )

    """ [Search bar] """
    search_fields = ("^city", "country", "^host__username", "host__gender")

    def count_amenities(self, obj):
        return obj.amenity.count()

    """ Customize column name """
    count_amenities.short_description = "Number of Amenities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Number of Photos"

    # @@@@@ [INSIDE Expression] @@@@@ #

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "address",
                    "prices",
                    "room_type",
                )
            },
        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "baths")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "More about the Space",
            {
                "classes": ("collapse",),  # Hide/Show (collapsable)
                "fields": ("amenity", "facility", "house_rules"),
            },
        ),
        (
            "Last Detail",
            {"fields": ("host",)},
        ),
    )

    """ filter_horizontal : Used for ManytoManyField """
    filter_horizontal = (
        "amenity",
        "facility",
        "house_rules",
    )

    raw_id_fields = ("host",)

    inlines = (PhotoInline,)

    def save_model(self, request, obj, form, change):
            #obj.user = request.user
            print(request.user)
            super().save_model(request, obj, form, change)

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Room Admin Deffinition  """

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        # print(dir(obj.file))
        return mark_safe(f'<img width="100px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"