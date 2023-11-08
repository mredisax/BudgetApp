from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # API endpoints for budgets
    path('transactions', views.TransactionListView.as_view(), name='transaction-list'),
    path('categories', views.TransactionCategoryView.as_view(), name='transaction-category'),
    path('tags', views.TransactionTagView.as_view(), name='transaction-tag'),

    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),

#     # API endpoints for transactions
#     path('api/transactions/', views.TransactionListView.as_view(), name='transaction-list'),
#     path('api/transactions/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction-detail'),

#     # API endpoints for creating budgets, tags, and categories
#     path('api/budgets/create/', views.BudgetCreateView.as_view(), name='budget-create'),
#     path('api/tags/create/', views.TagCreateView.as_view(), name='tag-create'),
#     path('api/categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
]
