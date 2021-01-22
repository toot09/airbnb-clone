from django.core.management.base import BaseCommand
from rooms import models as room_models

class Command(BaseCommand):
    help = 'This command creates facilities'

    def handle(self, *args, **options):
        room_models.Facility.objects.all().delete()
        facilities = (
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises,",
            "Elevator",
            "parking",
            "Gym",
        )
        for f in facilities:
            room_models.Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f'{len(facilities)} Facilities created!'))