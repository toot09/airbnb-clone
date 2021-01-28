from django.shortcuts import render
from django.http import HttpResponse

def all_rooms(request):
    #return HttpResponse(content="hello")
    return render(request, "all_rooms")
