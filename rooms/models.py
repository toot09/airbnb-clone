from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstactItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    """ https://docs.djangoproject.com/en/2.2/topics/db/models/ (About Meta class)"""

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstactItem):

    """ RoomType Models Definition """

    class Meta:
        " verbose_name : Customize name and django plus 's' after that"
        verbose_name = "Room Type"
        " Ordering by created date in AbstarctItem(core_models.TimeStampedModel)"
        ordering = ["created"]


class Amenity(AbstactItem):

    """ Amenity Models Demodelsfinition """

    class Meta:
        " verbose_name_plural : Customize all of name "
        verbose_name_plural = "Amenities"


class Facility(AbstactItem):

    """ Facility Models Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstactItem):

    """ HouseRule Models Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo Models Definition """

    caption = models.CharField(max_length=100)
    file = models.ImageField(upload_to="room_photos")
    " Can definite class for using String. Use this because of Error because python read code from top to bottom "
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    """ Room model custom """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    prices = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    """ [ForeignKey] Connect to the other models(users models) *import user models* """
    # related_name : customize name (org : room_set [objectname_set])
    host = models.ForeignKey(
        user_models.User, related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    """ ManyToMany is 多:多 Not 1:多 """
    amenity = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facility = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_rating = 0
        if (len(all_reviews)) == 0:
            return 0
        for review in all_reviews:
            all_rating += review.rating_average()
        return round(all_rating / len(all_reviews), 2)
