
from django.shortcuts import render
from .models import Plant


def all_plants(request):
    plants = Plant.objects.all()

    category = request.GET.get('category')
    is_edible = request.GET.get('is_edible')

    if category:
        plants = plants.filter(category=category)

    if is_edible in ['true', 'false']:
        plants = plants.filter(is_edible=(is_edible == 'true'))

    context = {
        'plants': plants,
        'categories': Plant.CategoryChoices.choices,
        'selected_category': category,
        'selected_edible': is_edible,
    }

    return render(request, 'plants/all_plants.html', context)
