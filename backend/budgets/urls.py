from django.urls import path
from . import views

urlpatterns = [
    path('budgets', views.BudgetListView.as_view(), name='budget-list'),
    path('budget/<int:budget_id>', views.BudgetDetailView.as_view(), name='budget-detail'),
    path('budget/create', views.BudgetCreateView.as_view(), name='budget-create'),
#     # API endpoints for creating budgets, tags, and categories
#     path('api/tags/create/', views.TagCreateView.as_view(), name='tag-create'),
#     path('api/categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
]
