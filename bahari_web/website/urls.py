from django.urls import path

from .views import about_us, index, menu

app_name = 'website'

urlpatterns = [
    path('', index, name='index'),
    path('about-us', about_us, name='about_us'),
    path('menu', menu, name='menu' ),
]