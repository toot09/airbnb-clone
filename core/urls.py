from django.urls import path
from rooms import views as room_views

# Specifying a namespace in urls.py(config)
app_name = "core"

urlpatterns = [
    #HomeView is Class. so return use "as_view" for return view shape
    path("",room_views.HomeView.as_view(), name="home"),
]