from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Enter Food", max_length=200)

class WorkoutResponse(forms.Form):
    response = forms.CharField(label="Enter a muscle group", max_length=100)

class CreateChatResponse(forms.Form):
    response = forms.CharField(label="Enter A Question", max_length=200)