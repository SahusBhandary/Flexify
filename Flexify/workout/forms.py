from django import forms

class WorkoutResponse(forms.Form):
    response = forms.CharField(label="Enter a muscle group", max_length=100)