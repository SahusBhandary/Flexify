from django.urls import path
from . import views

urlpatterns = [
    path('foodData/', views.foodData),
    path('foodData/nutrition', views.displayNutrition),
]