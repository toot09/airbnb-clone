from django.core.management.base import BaseCommand
from rooms import models as room_models

class Command(BaseCommand):
    help = 'This command creates rules'

    def handle(self, *args, **options):
        room_models.HouseRule.objects.all().delete()
        rules = (
            "No smoking.",
            "No parties or events.",
            "No pets/Pets allowed.",
            "No unregistered guests.",
            "No food or drink in bedrooms.",
            "No loud noise after 11 PM.",

        )
        for f in rules:
            room_models.HouseRule.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f'{len(rules)} rules created!'))