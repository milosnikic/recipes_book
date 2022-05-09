from django.urls import path

from . import views


urlpatterns = [
    path('', views.IngridientsListCreateAPIView.as_view(), name='list-ingridients'),
]
