from django.shortcuts import render
from . import models

def all_rooms(request):
    # USE GET Method
    page = int(request.GET.get("page",1))
    page_size = 10
    limit = page_size * page
    offset = page_size * (page-1)
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(request, "rooms/home.html", context={
        "rooms" : all_rooms
    })
