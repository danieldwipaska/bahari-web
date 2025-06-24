from django.http import HttpRequest, HttpResponse

from django.shortcuts import render

from bahari_web.apps.events.models import Event


def index(request: HttpRequest) -> HttpResponse:
    events = Event.objects.order_by('-start_date')[:3]
    
    context = {
        "title": "Bahari Irish Pub",
        "current_tab": "home",
        "events": events,
    }
    return render(request, "index.html", context)


def menu(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Menu - Bahari Irish Pub",
        "current_tab": "menu",
    }

    return render(request, "menu.html", context)
