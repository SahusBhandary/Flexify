from django import forms

class WorkoutResponse(forms.Form):
    CHOICES = [
        ("abdominals", "Abs"),
        ("abductors", "Abductors"),
        ("adductors", "Adductors"),
        ("biceps", "Biceps"),
        ("calves", "Calves"),
        ("chest", "Chest"),
        ("forearms", "Forearms"),
        ("glutes", "Glutes"),
        ("hamstrings", "Hamstrings"),
        ("lats", "Lats"),
        ("lower-back", "Lower Back"),
        ("middle_back", "Middle Back"),
        ("neck", "Neck"),
        ("quadriceps", "Quads"),
        ("traps", "Traps"),
        ("triceps", "Triceps"),
        
    ]
    name = forms.CharField(label="Workout Name", max_length=200)
    muscle_group = forms.ChoiceField(choices=CHOICES)
    
