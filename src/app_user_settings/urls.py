from django.urls import path

from . import views

urlpatterns = [
    path('settings/users', views.main_view, name='user-settings'),
    path('settings/', views.user_settings_view, name='main-settings')
]