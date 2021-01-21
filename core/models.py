from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    # auto_now_add : Update datetime when model is added
    # auto_now : update datetime when model is updated
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # What is abstract models?
    # Abstract models is not reflected to DB
    # Just used to be extended
    class Meta:
        abstract = True