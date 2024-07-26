from django.urls import path
from . import views

urlpatterns = [
    path('exercise/', views.exercise_API_req, name='create_workout'),
    path('workout/', views.redirectCreateWorkout),
    path('createWorkout/', views.redirectCreateWorkout),
    path('createWorkout/<str:username>/', views.displayWorkout, name='display_workout'),
    path('workout/<str:username>/<str:workoutName>', views.displayUserSpecificWorkout)
]