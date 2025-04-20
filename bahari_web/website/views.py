from django.http import HttpRequest, HttpResponse

from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Bahari Irish Pub",
        "current_tab": "home",
    }
    return render(request, "index.html", context)


def about_us(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "About Us - Bahari Irish Pub",
        "current_tab": "about_us",
    }

    return render(request, "about_us.html", context)


def menu(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Menu - Bahari Irish Pub",
        "current_tab": "menu",
    }

    return render(request, "menu.html", context)


def location(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Location - Bahari Irish Pub",
        "current_tab": "location",
    }

    return render(request, "location.html", context)


def event_gallery(request: HttpRequest) -> HttpResponse:
    context = {
        "title": "Event Gallery - Bahari Irish Pub",
        "current_tab": "event_gallery",
    }

    return render(request, "event_gallery.html", context)
