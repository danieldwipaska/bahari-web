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
