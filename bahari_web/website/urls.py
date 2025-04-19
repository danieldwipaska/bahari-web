from django.urls import path

from .views import about_us, index

app_name = 'website'

urlpatterns = [
    path('', index, name='index'),
    path('about-us', about_us, name='about_us'),
]