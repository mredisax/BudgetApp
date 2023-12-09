from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # API endpoints for budgets
    path('transactions', views.TransactionListView.as_view(), name='transaction-add'),
    path('transactions/<int:budget_id>/', views.TransactionListView.as_view(), name='transaction-list'),
    path('transaction/<int:budget_id>/<int:pk>', views.TransactionDetailView.as_view(), name='transaction-edit'),
    path('categories', views.TransactionCategoryView.as_view(), name='transaction-category'),
    path('tags', views.TransactionTagView.as_view(), name='transaction-tag'),
]
