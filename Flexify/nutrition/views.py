from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from foodAPI import food, findNutrition, nutrients
from .forms import CreateNewList, DietForm, FoodForm
from main.models import Diet, User

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

def diets(request):
    if request.method == "POST":
        form = DietForm(request.POST)

        if form.is_valid():
            new_diet_name = form.cleaned_data.get('name')
            User.objects.get(username=request.user.username).diet_set.create(name=new_diet_name)
            return render(request,'main/diets.html', {"form": form, "diets_list": User.objects.get(username=request.user.username).diet_set.all()})
    else: 
        form = DietForm()
        return render(request,'main/diets.html', {"form": form, "diets_list": User.objects.get(username=request.user.username).diet_set.all()})
    
def displaySpecificDiet(request, id):
    if request.method == "POST":
        form = FoodForm(request.POST)

        if form.is_valid():
            name_of_food = form.cleaned_data.get('name')
            User.objects.get(username=request.user.username).diet_set.all().get(name=id).fooditem_set.create(text=name_of_food)

    form = FoodForm()
    return render(request, 'main/specific_diet.html', {"form": form, "diet_name": id, "food_list": User.objects.get(username=request.user.username).diet_set.all().get(name=id).fooditem_set.all()})