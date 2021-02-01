from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    # USE GET Method
    page = request.GET.get("page")
    room_list = models.Room.objects.all()

    #Pagination (https://docs.djangoproject.com/en/2.2/topics/pagination/)
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    return render(request, "rooms/home.html", {"rooms" :rooms})
