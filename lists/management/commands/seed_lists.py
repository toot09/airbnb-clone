import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models

NAME = "lists"

class Command(BaseCommand):
    help = f'This command creates many {NAME}'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int ,help=f"How many {NAME} do you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        seeder.add_entity(list_models.List, number, {
            "name": lambda x:seeder.faker.address(),
            "user": lambda x:random.choice(all_users),
        },)
        seeder_pk = seeder.execute()
        for pk in flatten(seeder_pk.values()):
            lists = list_models.List.objects.get(pk=pk) 
            room = room_models.Room.objects.all()
            to_add = room[random.randint(0,5): random.randint(6,10)]
            # "*" means I wanna use only data in array, not array type data 
            lists.room.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))