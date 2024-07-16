from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexFunction():
    return 1
def displayNutrition():
    return HttpResponse("hi")

def index():
    return 2
