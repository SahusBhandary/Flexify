from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from .forms import WorkoutResponse
from workout.models import UserWorkoutHistory, Workouts
from main.models import User
from django.contrib.auth.decorators import login_required
from Workout import Workout

# Create your views here.
def displayWorkout(request):
    full_list = request.session.get("listExercises", "")
    return render(request, 'main/createWorkout.html', {})

def generate_list(muscle):
    listExercises = []
    api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
    response = requests.get(api_url, headers={'X-Api-Key': 'Ynv9N0AgZh7W0SnR3TxOpA==k1ucv8udqf3FRxIf'})
    if response.status_code == requests.codes.ok:
        exercises = response.json()
        for exercise in exercises:
            listExercises.append(exercise['name'])       
    else:
        print("Error:", response.status_code, response.text)
    return listExercises

def encrypt_workout(username, workoutName):
    lengthUsername = len(username)
    lengthWorkout = len(workoutName)
    return str(lengthUsername) + "#" + str(lengthWorkout) + "#" + username + "#" + workoutName

def valid_workoutName(workoutName, username):
    # filter by username + #
    # decode the string so we can find the workout name
    # if the workoutname already exists in the db, thrown an error
    workout_set = Workouts.objects.filter(workout_name__contains = (username + '#'))
    for workouts in workout_set:
        db_workout_name = decode_workout(workouts.workout_name)
        print(db_workout_name)
        if workoutName == db_workout_name:
            return False
    return True

def get_workout_exercises(workoutName, username):
    exercises = []
    workout_set = Workouts.objects.filter(workout_name__contains = (username + '#'))
    for workouts in workout_set:
        db_workout_name = decode_workout(workouts.workout_name)
        if workoutName == db_workout_name:
            exercises.append(workouts.exercise_name)
    return exercises

def decode_workout(encryptedString):
    i = 0
    len = ""
    while encryptedString[i] != "#":
        len += encryptedString[i]
        i+=1
    usernameLength = int(len)
    i+=1
    len = ""
    while encryptedString[i] != "#":
        len += encryptedString[i]
        i+=1
    workout_length = int(len)
    i+=1
    for j in range(1, usernameLength + 1):
        j+=1
    decodedString = ""
    for k in range((j + i), ((j + i) + workout_length), 1):
        decodedString += encryptedString[k]
    return decodedString

def exercise_API_req(request):
    listExercises = []
    canDisplay = False
    displayError = False
    username = request.user.username
    muscle = ""
    if request.method == "POST":
        if 'save_muscle' in request.POST:
            form = WorkoutResponse(request.POST)
            if form.is_valid():
                canDisplay = True
                muscle = form.cleaned_data["muscle_group"]
                listExercises = generate_list(muscle)
        elif 'add_items' in request.POST:
            form = WorkoutResponse(request.POST)
            if form.is_valid():
                user_model = User.objects.get(username=username)
                muscle = form.cleaned_data["muscle_group"]
                workoutName = form.cleaned_data["name"]
                if valid_workoutName(workoutName, username) == False:
                    displayError = True
                else:
                    displayError = False
                    selectedExercises = []
                    print(muscle)
                    listExercises = generate_list(muscle)
                    for i, e in enumerate(listExercises, start=1):
                        checkbox_name = 'workout_' + str(i)
                        if checkbox_name in request.POST:
                            selectedExercises.append(e)
                    
                    new_workout = UserWorkoutHistory(user_account_id=user_model.username, workout_name=workoutName)
                    new_workout.save()
                    for e in selectedExercises:
                        new_exercise = Workouts(workout_name=encrypt_workout(username, workoutName),exercise_name=e)
                        new_exercise.save()
    else:
        canDisplay = False
        form = WorkoutResponse()

    
    
    return render(request, "main/exercise.html", {"form":form, "displayContent":canDisplay, "workout_list": listExercises, "displayError": displayError})

