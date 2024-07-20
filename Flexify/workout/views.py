from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from .forms import WorkoutResponse, CreateNewWorkout
from workout.models import UserWorkoutHistory
from django.contrib.auth.decorators import login_required

"""
- Make the exercise in model an array
- If the exercise is checked, add it to the list
- Make a create new workout thing where they can select workouts and save it
"""

# Create your views here.
def displayWorkout(request):
    full_list = request.session.get("listExercises", "")
    return render(request, 'main/createWorkout.html', {})

def exercise_API_req(request):
    listExercises = []
    canDisplay = False
    if request.method == "POST":
        form = WorkoutResponse(request.POST)
        workoutNameForm = CreateNewWorkout(request.POST)
        

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
        if workoutNameForm.is_valid():
            username = request.user.username
            workoutName = workoutNameForm.cleaned_data["name"]
            newWorkout = UserWorkoutHistory(user=username, workout_name=workoutName, workout_list=[])
            newWorkout.save()
    else:
        canDisplay = False
        form = WorkoutResponse()
        workoutNameForm = CreateNewWorkout()

    return render(request, "main/exercise.html", {"form":form, "workoutFormName": workoutNameForm, "displayContent":canDisplay, "workout_list": listExercises})

