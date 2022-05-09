from django.urls import path

from . import views


urlpatterns = [
    path('', views.RecipesListCreateAPIView.as_view(), name='recipe-list'),
    path('<int:pk>/', views.RecipeRetrieveAPIView.as_view(), name='recipe-detail'),
    path('<int:pk>/rate', views.RatingCreateAPIView.as_view(), name='recipe-rate'),
]
