from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # API endpoints for budgets
    path('transactions/<int:budget_id>/', views.TransactionListView.as_view(), name='transaction-list'),
    path('transaction/<int:budget_id>/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction-edit'),
    path('categories', views.TransactionCategoryView.as_view(), name='transaction-category'),
    path('tags', views.TransactionTagView.as_view(), name='transaction-tag'),

#     # API endpoints for transactions
#     path('api/transactions/', views.TransactionListView.as_view(), name='transaction-list'),
#     path('api/transactions/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction-detail'),

#     # API endpoints for creating budgets, tags, and categories
#     path('api/budgets/create/', views.BudgetCreateView.as_view(), name='budget-create'),
#     path('api/tags/create/', views.TagCreateView.as_view(), name='tag-create'),
#     path('api/categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
]
