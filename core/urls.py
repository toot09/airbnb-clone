from django.urls import path
from rooms import views as room_views

# Specifying a namespace in urls.py(config)
app_name = "core"

urlpatterns = [
    path("",room_views.all_rooms, name="home"),
]