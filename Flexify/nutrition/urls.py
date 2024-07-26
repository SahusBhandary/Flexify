from django.urls import path
from . import views

urlpatterns = [
    path('foodData/', views.foodData, name='nutrition'),
    path('foodData/nutrition', views.displayNutrition),
    path('foodData/added', views.added),
    path('foodData/removed', views.removed),
    path('diets/', views.diets),
    path('diets/<str:id>/', views.displaySpecificDiet)
]