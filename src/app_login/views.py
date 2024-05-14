from django.shortcuts import render

# Create your views here.

def login_view(request):
    name = "Login"
    return render(request, 'app_login/index.html', {'name': name})
