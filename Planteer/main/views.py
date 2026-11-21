from django.shortcuts import render
from plants.models import Plant


def home(request):
    plants = Plant.objects.all()[:3]

    context = {
        'plants': plants
    }

    return render(request, 'main/home.html', context)