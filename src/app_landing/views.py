from django.shortcuts import render


def my_view(request):
    name = "Landing"

    return render(request, 'template.html', {'name': name})