from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # API endpoints for budgets
    path('stats/<int:budget_id>', views.StatisticsListView.as_view(), name='stats-list'),

]
