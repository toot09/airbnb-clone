from django.utils import timezone
from django.shortcuts import render
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
    return render(request, "rooms/detail.html")
