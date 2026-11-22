
from django.shortcuts import render, redirect
from .models import Plant
from .forms import PlantForm


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


def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('all_plants')
    else:
        form = PlantForm()

    return render(request, 'plants/add_plant.html', {'form': form})
