from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Food", max_length=200)