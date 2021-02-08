from django.utils import timezone
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView
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

def room_detail(request, pk):
    # Parma "pk" received in rooms/urls.py
    try:
        room = models.Room.objects.get(pk=pk)
        #{'room':room} => content
        return render(request, "rooms/detail.html", {'room':room})
    except models.Room.DoesNotExist:
        #return redirect(reverse("core:home"))
        #return redirect(reverse("rooms:detail",kwargs={"pk":247}))
        #from django.http import Http404
        raise Http404()
    
