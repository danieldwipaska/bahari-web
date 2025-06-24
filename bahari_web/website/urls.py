from django.urls import path

from .views import index, menu

app_name = "website"

urlpatterns = [
    path("", index, name="index"),
    path("menu", menu, name="menu"),
]
