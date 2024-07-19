from django.db import models

# Create your models here.
class UserWorkouts(models.Model):
    user = models.CharField(max_length=200)
    exercise = models.CharField(max_length=200)
    ifChosen = models.BooleanField(default=False)

    def __str__(self):
        return self.user