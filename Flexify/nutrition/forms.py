from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Enter Food", max_length=200)

class DietForm(forms.Form):
    name = forms.CharField(label="Name of Diet", max_length=200)

class FoodForm(forms.Form):
    name = forms.CharField(label="Food to add", max_length=200)