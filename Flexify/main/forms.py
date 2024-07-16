from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Enter Food", max_length=200)