from django.urls import path

from .views import about_us, event_gallery, index, location, menu

app_name = "website"

urlpatterns = [
    path("", index, name="index"),
    path("about-us", about_us, name="about_us"),
    path("menu", menu, name="menu"),
    path("location", location, name="location"),
    path("event-gallery", event_gallery, name="event_gallery"),
]
