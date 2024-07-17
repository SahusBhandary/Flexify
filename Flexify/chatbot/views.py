from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CreateChatResponse
from openai import OpenAI
import requests
OPENAI_API_KEY = "sk-proj-9HmSSHn6fwKlflozExIaT3BlbkFJE72fz6rIBf4yWwz3w4Vn"
client = OpenAI(api_key=OPENAI_API_KEY)

# Create your views here.
def display(request):
    full_message = request.session.get("full_message", "")
    return render(request, 'main/index.html', { "name": full_message})

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
    return render(request, "main/create.html", {"form":form})