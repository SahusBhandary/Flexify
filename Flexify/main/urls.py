from django.urls import path
from . import views

urlpatterns = [
    path('foodData/', views.foodData),
    path('', views.default),
    path('foodData/nutrition', views.displayNutrition),
    path("<str:id>", views.index)
]