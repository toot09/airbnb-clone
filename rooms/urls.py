from django.urls import path
from . import views

# Specifying a namespace in urls.py(config)
app_name = "rooms"

# URL Dispatcher (like <int:year> ~) : https://docs.djangoproject.com/en/3.1/topics/http/urls/
urlpatterns = [
    path("<int:pk>", views.RoomDetail.as_view(), name="detail"),
    path("search/", views.Search, name="search"),
]