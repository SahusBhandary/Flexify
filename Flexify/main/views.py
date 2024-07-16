from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from foodAPI import food, findNutrition
from .forms import CreateNewList, WorkoutResponse, CreateChatResponse
from .models import Food

from openai import OpenAI
import requests
OPENAI_API_KEY = "sk-proj-6Kod05mOaf7ZOgiuIn3QT3BlbkFJ92Wjrx4IHjy4hSCiuMh9"
client = OpenAI(api_key=OPENAI_API_KEY)

# Create your views here.
def foodData(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)
        
        if form.is_valid():
            food["userFood"] = form.cleaned_data["name"]
        
        return HttpResponseRedirect('nutrition')
    else:
        form = CreateNewList()
        return render(request, 'foodData.html', {"form": form})

def displayNutrition(request):
    return render(request, 'nutrition.html', {"foodName": food["userFood"], "foodData": findNutrition(food["userFood"])})

def index(response, id):
    ls = Food.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" % ls.name)

def default(request):
    return render(request, 'default.html', {"data": food})

# Create your views here.
def display(request):
    full_message = request.session.get("full_message", "")
    return render(request, 'index.html', { "name": full_message})

def home (response):
    return render(response, "home.html", {"name": "test"})

def create(request):
    if request.method == "POST":
        form = CreateChatResponse(request.POST)
        
        if form.is_valid():
            print("is valid")
            # Message list for sample response
            userMessage = form.cleaned_data["response"]
            message_list = [
            {
                "role": "system",
                "content": "I am a fitness expert trained in nutrition and lifting weights",
            },
            {"role": "user", "content": userMessage},
            ]
            chat_completion = client.chat.completions.create(
                messages=message_list,
                model="gpt-3.5-turbo",
            )
            full_message = chat_completion.choices[0].message.content
            request.session["full_message"] = full_message
            return HttpResponseRedirect("/display")
    else:
        form = CreateChatResponse()
    return render(request, "create.html", {"form":form})

def exercise_API_req(request):
    if request.method == "POST":
        form = WorkoutResponse(request.POST)

        if form.is_valid():
            muscle = form.cleaned_data["response"]
            api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
            response = requests.get(api_url, headers={'X-Api-Key': 'Ynv9N0AgZh7W0SnR3TxOpA==k1ucv8udqf3FRxIf'})
            if response.status_code == requests.codes.ok:
                exercises = response.json()
                full_message = ""
                for exercise in exercises:
                    full_message += exercise['name'] + " "
                request.session["full_message"] = full_message
                return HttpResponseRedirect("/display")
            else:
                print("Error:", response.status_code, response.text)
    else:
        form = WorkoutResponse()
    return render(request, "exercise.html", {"form":form})