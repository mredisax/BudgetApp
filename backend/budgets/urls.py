from django.urls import path
from . import views

urlpatterns = [
    path('budgets/<int:budget_id>/', views.BudgetDetailView.as_view(), name='budget-detail'),
#     # API endpoints for creating budgets, tags, and categories
#     path('api/budgets/create/', views.BudgetCreateView.as_view(), name='budget-create'),
#     path('api/tags/create/', views.TagCreateView.as_view(), name='tag-create'),
#     path('api/categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
]
