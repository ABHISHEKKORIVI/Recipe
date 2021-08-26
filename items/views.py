from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Recipes


def home(request):
    return render(request, 'items/home.html')


#1Creating
def create(request):
    return render(request, 'items/create.html')


''' Url path(create) will request to create views logic
    and this create views will request create.html to add recipes'''


#2 Posting to database
def data(request):
    if request.method == "POST":
        Recipes.objects.create(
            name=request.POST["name"],
            ingredients = request.POST["ingredients"],
            process=request.POST["process"],
            #image=request.FILES["image"]
        )
        return HttpResponseRedirect('/items/recipe_list/')
    return render (request, 'items/create.html')


''' After creating recipes in create.html it will requests post the data to data which will be stored in 
    Recipes data base(ORM) and redirects to recipelist(list.html) '''

#3 Fetching Database


def recipe_list(request):
    recipe=Recipes.objects.all()
    return render(request, 'items/list.html', {'recipe': recipe})


''' In this recipe list we can get all data of recipes that are stored in Recipes database'''

#4 Details of recipe


def details(request, recipe_id):
    recipe = Recipes.objects.get(id=recipe_id)
    return render(request, 'items/details.html', {'recipe':recipe})


''' By clicking on recipe name in recipelist(list.html) we can get details of recipe like name, ingredients etc..'''

#5 Update recipe


def update(request, recipe_id):
    
    if request.method == 'GET':
        up= Recipes.objects.get(id=recipe_id)
        return render(request, 'items/update.html', {'up': up})

    else:
        recipe = Recipes.objects.get(id=recipe_id)
        recipe.name = request.POST['name']
        recipe.ingredients = request.POST['ingredients']
        recipe.process = request.POST['process']
        recipe.save()
        r = Recipes.objects.get(id=recipe_id)
        print(r.id)
        return HttpResponseRedirect(reverse('items:recipe_list'))
      

''' update recipe details like name or ingredients, process by geting data and post to database '''

#6 Delete recipe


def delete(request, recipe_id):
    recipe = Recipes.objects.get(id=recipe_id)
    recipe.delete()
    return HttpResponseRedirect(reverse('items:recipe_list'))




