from django.urls import path
from . import views

urlpatterns = [
    # API endpoints for budgets
    path('api/transactions/', views.TransactionListView.as_view(), name='transaction-list'),

    path('api/budgets/<int:budget_id>/', views.BudgetDetailView.as_view(), name='budget-detail'),

    path('api/categories', views.TransactionCategoryView.as_view(), name='transaction-category'),
#     # API endpoints for transactions
#     path('api/transactions/', views.TransactionListView.as_view(), name='transaction-list'),
#     path('api/transactions/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction-detail'),

#     # API endpoints for creating budgets, tags, and categories
#     path('api/budgets/create/', views.BudgetCreateView.as_view(), name='budget-create'),
#     path('api/tags/create/', views.TagCreateView.as_view(), name='tag-create'),
#     path('api/categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
]