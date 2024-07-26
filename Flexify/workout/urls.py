from django.urls import path
from . import views

urlpatterns = [
    path('exercise/', views.exercise_API_req, name='exercise_api_req'),
    path('workout/', views.redirectCreateWorkout),
    path('createWorkout/', views.redirectCreateWorkout),
    path('createWorkout/<str:username>/', views.displayWorkout, name='display_workout'),
    path('workout/<str:username>/<str:workoutName>', views.displayUserSpecificWorkout)
]