from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from .forms import WorkoutResponse

# Create your views here.
def displayWorkout(request):
    full_list = request.session.get("listExercises", "")
    return render(request, 'main/workoutDisplay.html', { "name": full_list})

def exercise_API_req(request):
    if request.method == "POST":
        print("Post")
        form = WorkoutResponse(request.POST)

        if form.is_valid():
            muscle = form.cleaned_data["response"]
            api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
            response = requests.get(api_url, headers={'X-Api-Key': 'Ynv9N0AgZh7W0SnR3TxOpA==k1ucv8udqf3FRxIf'})
            if response.status_code == requests.codes.ok:
                exercises = response.json()
                listExercises = ""
                for exercise in exercises:
                    print(listExercises)
                    listExercises += exercise['name'] + " "
                request.session["listExercises"] = listExercises
                return HttpResponseRedirect("/displayWorkout")
            else:
                print("Error:", response.status_code, response.text)
    else:
        form = WorkoutResponse()
    return render(request, "main/exercise.html", {"form":form})

