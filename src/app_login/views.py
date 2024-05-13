from django.shortcuts import render

# Create your views here.

def login_view(request):
    name = "Login"
    return render(request, 'template.html', {'name': name})
