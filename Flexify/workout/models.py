from django.db import models
from django.contrib.postgres.fields import ArrayField
# pip install psycopg2 
# Create your models here.
class UserWorkoutHistory(models.Model):
    user = models.CharField(max_length=200)
    workout_name = models.CharField(max_length=200)
    workout_list = ArrayField(models.CharField(max_length=50), blank=True, default=list)

    def __str__(self):
        return self.workout_name