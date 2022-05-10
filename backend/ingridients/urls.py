from django.urls import path

from . import views


urlpatterns = [
    path('', views.IngridientsListCreateAPIView.as_view(), name='ingridients-list'),
    path('most-used/', views.IngridientsMostUsedListAPIView.as_view(), name='most-used-ingridients-list'),
]
