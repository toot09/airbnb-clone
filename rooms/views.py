from datetime import datetime
from django.shortcuts import render

def all_rooms(request):
    now = datetime.now()
    diet = True
    return render(request, "all_rooms.html", context={
        "now" : now,
        "diet": diet,
    })
