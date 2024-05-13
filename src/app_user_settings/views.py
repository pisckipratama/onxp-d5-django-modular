from django.shortcuts import render

# Create your views here.

def user_settings_view(request):
    name = "User Settings"

    return render(request, 'template.html', {'name': name})