from django.db import models

# Create your models here.



#models da minha Recipes

class Recipe(models.Model):
    recipe_name = models.CharField(max_length = 100)
    description = models.TextField(max_length=100)
    images = models.ImageField(upload_to='recipes/recipes_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)