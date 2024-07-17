from django import forms

class CreateChatResponse(forms.Form):
    response = forms.CharField(label="Enter A Question", max_length=200)