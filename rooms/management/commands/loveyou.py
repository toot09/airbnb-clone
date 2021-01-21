from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Yes! correct!"

    def add_arguments(self, parser):
        parser.add_argument("--times",help="???")

    def handle(self, *args, **options):
        print(args)
        print(options)
        times = options.get("times")
        for i in range(int(times)):
            print("I love you")
        