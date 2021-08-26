from django.db import models

class Recipes(models.Model):
    name = models.CharField(max_length=25)
    ingredients = models.TextField(max_length=200)
    process = models.TextField()
    #image = models.ImageField(upload_to='images/',null=True)
    def __str__(self):
        return self.name

