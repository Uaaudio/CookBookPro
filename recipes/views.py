from django.shortcuts import render

# Create your views here.

def recipes_page(request):
    return render (request, "recipes.html")