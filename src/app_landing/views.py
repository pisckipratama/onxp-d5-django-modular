from django.shortcuts import render


def my_view(request):
    return render(request, 'app_landing/index.html', { 'name': 'Landing' })

def about_view(request):
    return render(request, 'app_landing/about.html', {'name': 'About'})