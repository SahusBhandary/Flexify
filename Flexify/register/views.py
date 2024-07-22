from django.shortcuts import render
from django.urls import reverse
from workout.models import UserWorkoutHistory
from .forms import RegisterForm
from main.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            new_user = User(username=name)
            new_user.save()
            new_workout_history = UserWorkoutHistory(user_account=new_user, workout_name="")
            new_workout_history.save()
            form.save()
            return HttpResponseRedirect("/login")
    else:
        form = RegisterForm()
    
    form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

