import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models

class Command(BaseCommand):
    help = 'This command creates many rooms'

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int ,help="How many rooms do you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        all_users = user_models.User.objects.all()
        all_roomTypes = room_models.RoomType.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(room_models.Room, number, {
            # Use Faker
            "name": lambda x:seeder.faker.address(),
            # Foreign Key Setting (seeder can't match FK)
            "host": lambda x:random.choice(all_users),
            "room_type": lambda x:random.choice(all_roomTypes),
            "prices": lambda x : random.randint(140000, 500000),
            "guests": lambda x : random.randint(2,10),
            "beds": lambda x : random.randint(1,4),
            "bedrooms": lambda x : random.randint(1,5),
            "baths": lambda x : random.randint(1,3),
            #'is_staff':False,
        },)
        # seeder.execute() return Primary Key
        create_photos = seeder.execute()
        #print(create_photos.values()) #2D Array returned
        for pk in flatten(create_photos.values()):
            room = room_models.Room.objects.get(pk=pk)
            amenity = room_models.Amenity.objects.all()
            facility = room_models.Facility.objects.all()
            rule = room_models.HouseRule.objects.all()
            for i in range(3,random.randint(10,17)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"/room_photos/{random.randint(1,31)}.webp",
                    room=room,
                )
            for a in amenity:
                if random.randint(0,15) % 2 == 0:
                    #ManytoMany Field add like below(.add)
                    room.amenity.add(a)
            for f in facility:
                if random.randint(0,15) % 2 == 0:
                    #ManytoMany Field add like below(.add)
                    room.facility.add(f)
            for r in rule:
                if random.randint(0,15) % 2 == 0:
                    #ManytoMany Field add like below(.add)
                    room.house_rules.add(r)
                
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))