from django.http import HttpRequest, HttpResponse

from django.shortcuts import render

from bahari_web.apps.events.models import Event
from bahari_web.apps.live_musics.models import LiveMusic


def index(request: HttpRequest) -> HttpResponse:
    events = Event.objects.filter(is_active=True).order_by('-start_date')[:3]
    live_musics = LiveMusic.objects.filter(is_active=True)

    context = {
        "title": "Bahari Irish Pub",
        "current_tab": "home",
        "events": events,
        "live_musics": live_musics,
    }
    return render(request, "index.html", context)


def menu(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Menu - Bahari Irish Pub",
        "current_tab": "menu",
    }

    return render(request, "menu.html", context)
