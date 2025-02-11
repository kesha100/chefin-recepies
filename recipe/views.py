from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Recipe, Category, Ingredient


# Category Views
class CategoryListView(ListView):
    model = Category
    template_name = 'recipes/category_list.html'
    context_object_name = 'categories'
    ordering = ['name']


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'recipes/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.filter(category=self.object)
        return context


class CategoryMixin(LoginRequiredMixin):
    model = Category
    fields = ['name', 'description']
    success_url = reverse_lazy('category-list')


class CategoryCreateView(CategoryMixin, CreateView):
    template_name = 'recipes/category_form.html'


class CategoryUpdateView(CategoryMixin, UpdateView):
    template_name = 'recipes/category_form.html'


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'recipes/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')


# Ingredient Views
class IngredientListView(ListView):
    model = Ingredient
    template_name = 'recipes/ingredient_list.html'
    context_object_name = 'ingredients'
    ordering = ['name']


class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'recipes/ingredient_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipes'] = self.object.recipes.all()
        return context


class IngredientMixin(LoginRequiredMixin):
    model = Ingredient
    fields = ['name']
    success_url = reverse_lazy('ingredient-list')


class IngredientCreateView(IngredientMixin, CreateView):
    template_name = 'recipes/ingredient_form.html'


class IngredientUpdateView(IngredientMixin, UpdateView):
    template_name = 'recipes/ingredient_form.html'


class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'recipes/ingredient_confirm_delete.html'
    success_url = reverse_lazy('ingredient-list')


# Enhanced Recipe Views
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    ordering = ['-created_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = self.object.ingredients.all()
        return context



class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    fields = ['title', 'text', 'image']
    success_url = reverse_lazy('recipes-home') 

class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'recipes/recipe_form.html'
    fields = ['title', 'text', 'image']
    success_url = reverse_lazy('recipes-home')



class RecipeDeleteView( DeleteView):
    model = Recipe
    template_name = 'recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipes-home')



# Search functionality
class SearchListView(ListView):
    model = Recipe
    template_name = 'recipes/search.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        category = self.request.GET.get('category')

        if q:
            q = q.lower()
            queryset = queryset.filter(
                Q(title__icontains=q) | 
                Q(text__icontains=q) |
                Q(ingredients__name__icontains=q)
            ).distinct()

        if category:
            queryset = queryset.filter(category__id=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

def wishes(request):
  return render(request, 'recipes/wishes.html')