from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from foodAPI import food, findNutrition, nutrients
from .forms import CreateNewList

# Create your views here.
def foodData(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        
        if form.is_valid():
            food["userFood"] = form.cleaned_data["name"]
        
        return HttpResponseRedirect('nutrition')
    else:
        form = CreateNewList()
        return render(request, 'main/foodData.html', {"form": form})

def displayNutrition(request):
    if request.method == "POST":
        return HttpResponse("added")
    return render(request, 'main/nutrition.html', {"foodName": food["userFood"], "foodData": findNutrition(food["userFood"]), "protein": nutrients["protein"], "fat": nutrients["fat"], "carbs": nutrients["carbs"], "water": nutrients["water"], "energy": nutrients["energy"], "caffeine": nutrients["caffeine"], "sugar": nutrients["sugar"], "fiber": nutrients["fiber"], "calcium": nutrients["calcium"], "iron": nutrients["iron"]})

def added(request):
    return render(request, 'main/added.html')

def removed(request):
    return render(request, 'main/removed.html')