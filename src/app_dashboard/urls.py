from django.urls import path
from app_dashboard import views

urlpatterns = [
    path('dashboard/', views.my_view, name="dashboard")
]