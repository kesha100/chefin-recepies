from django.urls import path
from . import views
urlpatterns = [
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('search', views.SearchListView.as_view(), name='search'),
    path('wishes/', views.wishes, name='wishes')
]