from django.shortcuts import render


def agregasi(num):
    return num + 1

def my_view(request):
    return render(request, 'app_landing/index.html', { 'name': 'Landing' })

def about_view(request, id: int = 0, year: int = 2024):
    

    context = {
        "nama": f"Piscki {id}",
        "agregasi": f"{agregasi(id)}",
        "year": year,
        "limit": request.GET.get("limit", 0)
    }
    return render(request, 'app_landing/about.html', context=context)