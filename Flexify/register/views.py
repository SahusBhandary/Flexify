from django.shortcuts import render
from .forms import RegisterForm
from .models import User

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            new_user = User(username=name)
            new_user.save()
            form.save()
    else:
        form = RegisterForm()
    
    form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

