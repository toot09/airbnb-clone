from django.views.generic import ListView
from . import models

class HomeView(ListView):
    
    """ HomeView Definition """
    model = models.Room
    # Attributes : https://ccbv.co.uk/projects/Django/2.2/django.views.generic.list/ListView/
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
