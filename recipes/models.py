from django.db import models

# Create your models here.



#models da minha Recipes

class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_email = models.EmailField(max_length=100)
    author_password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author_name


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    images = models.ImageField(upload_to='recipes/recipes_images/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.recipe_name