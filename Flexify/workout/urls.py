from django.urls import path
from . import views

urlpatterns = [
    path('exercise/', views.exercise_API_req, name='exercise_api_req'),
    path('createWorkout/', views.displayWorkout, name='display_workout'),
]