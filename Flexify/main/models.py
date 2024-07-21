from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Diet(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class FoodItem(models.Model):
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
