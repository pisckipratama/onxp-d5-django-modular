from django.shortcuts import render

# Create your views here.

def user_settings_view(request):
    name = "User Settings"
    return render(request, 'app_user_settings/settings.html', {'name': name})

def main_view(request):
    name = "Dashboard User Settings"
    return render(request, 'app_user_settings/index.html', {'name': name})