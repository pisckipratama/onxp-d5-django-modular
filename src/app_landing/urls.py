from django.urls import path

from .views import my_view, about_view


urlpatterns = [
    path('', my_view, name="home"),
    path('about/', about_view, name="about")
]