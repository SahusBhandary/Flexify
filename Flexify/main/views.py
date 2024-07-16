from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from foodAPI import food, findNutrition
from .forms import CreateNewList
from .models import Food

# Create your views here.
def foodData(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        
        if form.is_valid():
            food["userFood"] = form.cleaned_data["name"]
        
        return HttpResponseRedirect('nutrition')
    else:
        form = CreateNewList()
        return render(request, 'foodData.html', {"form": form})

def displayNutrition(request):
    return render(request, 'nutrition.html', {"foodName": food["userFood"], "foodData": findNutrition(food["userFood"])})

def index(response, id):
    return HttpResponse("<h1>%s</h1>" % findNutrition(id))

def default(request):
    return render(request, 'default.html', {"data": food})
