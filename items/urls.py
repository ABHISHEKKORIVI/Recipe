from django.urls import path
from.import views

app_name = "items"

urlpatterns = [
    path('home/',views.home, name='Home'),
    path('create/', views.create, name='create'),
    path('data/', views.data, name='data'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('<int:recipe_id>/details/', views.details, name='details'),
    path('<int:recipe_id>/update/', views.update, name='update'),
    path('<int:recipe_id>/delete/', views.delete, name='delete'),

         ]

