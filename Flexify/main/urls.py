from django.urls import path
from . import views

urlpatterns = [
    path('foodData/', views.foodData),
    path('', views.default),
    path('foodData/nutrition', views.displayNutrition),
    path("create/", views.create, name = "create"),
    path("display/", views.display, name = "display"),
    path("exercise/", views.exercise_API_req, name = "exercise_API_req"),
]