from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Recipe
# Create your views here.

def home(request):
  recipes = Recipe.objects.all()
  context = {
    'recipes': recipes
  }
  return render(request, 'recipes/home.html', context)





class RecipeListView(ListView):
  model = Recipe
  template_name = 'recipes/home.html'
  context_object_name = 'recipes'


class RecipeDetailView(DetailView):
  model = Recipe
  template_name = 'recipes/recipe_detail.html'
  context_object_name = 'object'


class SearchListView(ListView):
  model = Recipe
  template_name = 'recipes/search.html'
  context_object_name = 'recipes'

  def get_queryset(self):
    queryset = super().get_queryset()
    q = self.request.GET.get('q')
    if q:
      q = q.lower()  # Convert the search query to lowercase
      queryset = queryset.filter(Q(title__icontains=q) | Q(text__icontains=q))
    return queryset

def wishes(request):
  return render(request, 'recipes/wishes.html', {'title': 'Thank you for this Incubator!'})