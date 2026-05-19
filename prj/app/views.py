from django.shortcuts import render
from django.http import JsonResponse
from .models import Taktika


# HTML stránky

def render_homepage(request):
    return render(request, "home.html")


def render_about(request):
    return render(request, "about.html")


def render_api_playground(request):
    return render(request, "api_playground.html")


# API endpoint

def taktiky_api(request):
    taktiky = Taktika.objects.all()

    data = []

    for taktika in taktiky:
        data.append({
            "id": taktika.id,
            "name": taktika.name,
            "difficulty": taktika.difficulty,
            "effectivity": taktika.effectivity,
            "usefulness": taktika.usefulness,
        })

    return JsonResponse(data, safe=False)
