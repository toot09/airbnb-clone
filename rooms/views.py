from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
    # USE GET Method
    page = request.GET.get("page",1)
    room_list = models.Room.objects.all()

    #Pagination (https://docs.djangoproject.com/en/2.2/topics/pagination/)
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.get_page(int(page))
        return render(request, "rooms/home.html", {"page" :rooms})
    except Exception:
        return redirect("/")