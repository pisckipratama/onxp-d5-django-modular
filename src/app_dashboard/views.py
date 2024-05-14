from django.shortcuts import render

# Create your views here.

def my_view(request):
    name = "Dashboard"

    return render(request, 'app_dashboard/index.html', {'name': name})