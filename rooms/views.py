from django.utils import timezone
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django_countries import countries
from . import models

#Class Based View (CBV)
class HomeView(ListView):
    
    """ HomeView Definition """

    model = models.Room
    # Attributes : https://ccbv.co.uk/projects/Django/2.2/django.views.generic.list/ListView/
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     now = timezone.now()
    #     context["now"] = now
    #     return context

# CBV(Class Based View)
class RoomDetail(DetailView):
    
    """ RoomDetail Definition """
    model = models.Room
    # Attributes : http://ccbv.co.uk/projects/Django/3.0/django.views.generic.detail/DetailView/
    pk_url_kwarg = 'pk'


# FBV(Function Based View)
"""
def room_detail(request, pk):
    # Param "pk" received in rooms/urls.py
    try:
        room = models.Room.objects.get(pk=pk)
        #{'room':room} => content
        return render(request, "rooms/detail.html", {'room':room})
    except models.Room.DoesNotExist:
        #return redirect(reverse("core:home"))
        #return redirect(reverse("rooms:detail",kwargs={"pk":247}))
        #from django.http import Http404
        raise Http404()
"""
#Get countries : https://github.com/SmileyChris/django-countries#the-country-object
def Search(request):
    city = request.GET.get("city","anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country","KR")
    room_type = int(request.GET.get("room_type",0))
    room_types = models.RoomType.objects.all()
    
    form = {
        "city":city, 
        "s_country":country, 
        "s_room_type":room_type,
    }

    choices = {
        "countries":countries, 
        "room_types":room_types,
    }

    return render(
        request, 
        "rooms/search.html", 
        {**form,**choices,},
    )