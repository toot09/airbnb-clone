from django.db import models
from django.utils import timezone
from core import models as core_models
from rooms import models as room_models


class Reservation(core_models.TimeStampedModel):

    """ Reservation Models Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCLED = "cancled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCLED, "Cancled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE, null=True
    )
    room = models.ForeignKey(
        room_models.Room,
        related_name="reservations",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f"{self.room} ({self.check_in}~{self.check_out})"

    def in_progress(self):
        now = timezone.now().date()
        return self.check_in <= now and now <= self.check_out

    # Descript def boolean date to X or O emoji
    in_progress.boolean = True

    in_progress.short_description = "PROGRESS"

    def is_finished(self):
        now = timezone.now().date()
        return self.check_out < now

    is_finished.boolean = True
    is_finished.short_description = "FINISHED"