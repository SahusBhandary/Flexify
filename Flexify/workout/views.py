from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from .forms import WorkoutResponse
from workout.models import UserWorkouts
from django.contrib.auth.decorators import login_required

"""
- Make the exercise in model an array
- If the exercise is checked, add it to the list
- Make a create new workout thing where they can select workouts and save it
"""

# Create your views here.
def displayWorkout(request):
    full_list = request.session.get("listExercises", "")
    return render(request, 'main/workoutDisplay.html', { "workout_list": full_list})

def exercise_API_req(request):
    listExercises = []
    canDisplay = False
    if request.method == "POST":
        form = WorkoutResponse(request.POST)
        username = request.user.username
        newWorkout = UserWorkouts(user=username, exercise="", ifChosen=False)
        newWorkout.save()

        if form.is_valid():
            canDisplay = True
            muscle = form.cleaned_data["muscle_group"]
            api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
            response = requests.get(api_url, headers={'X-Api-Key': 'Ynv9N0AgZh7W0SnR3TxOpA==k1ucv8udqf3FRxIf'})
            if response.status_code == requests.codes.ok:
                exercises = response.json()
                for exercise in exercises:
                    listExercises.append(exercise['name'])
                request.session["listExercises"] = listExercises
            else:
                print("Error:", response.status_code, response.text)
    else:
        canDisplay = False
        form = WorkoutResponse()
    return render(request, "main/exercise.html", {"form":form, "displayContent":canDisplay, "workout_list": listExercises})

