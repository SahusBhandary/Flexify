from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.username
    
class Diet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class FoodItem(models.Model):
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
    
