from django.urls import path

from . import views


urlpatterns = [
    path('', views.RecipesListCreateAPIView.as_view()),
]
