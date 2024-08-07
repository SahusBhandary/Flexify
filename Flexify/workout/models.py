from django.db import models
from django.contrib.postgres.fields import ArrayField
from main.models import User
# pip install psycopg2 
# Create your models here.
class UserWorkoutHistory(models.Model):
    user_account = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_name = models.CharField(max_length=200)

    def __str__(self):
        return self.workout_name
    
class Workouts(models.Model):
    userworkouthistory = models.ForeignKey(UserWorkoutHistory, on_delete=models.CASCADE)
    workout_name = models.CharField(max_length=200)
    exercise_name = models.CharField(max_length=200)

    def __str__(self):
        return self.workout_name