from django.urls import path

from . import views


urlpatterns = [
    path('', views.RecipesListCreateAPIView.as_view(), name='recipe-list'),
    path('own/', views.RecipesOwnListAPIView.as_view(), name='recipe-own-list'),
    path('<int:pk>/', views.RecipeRetrieveAPIView.as_view(), name='recipe-detail'),
    path('rate/', views.RatingCreateAPIView.as_view(), name='recipe-rate'),
]
