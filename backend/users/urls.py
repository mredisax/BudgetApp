from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('auth/register', views.RegisterView.as_view(), name='register'),
    # path('auth/login', views.CustomObtainAuthToken.as_view(), name='login'),
        # path('auth/logout', views.LogoutView.as_view(), name='logout'),
    path('auth/register/', views.RegistrationView.as_view(), name='register'),
    path('auth/login/', views.LoginView.as_view(), name='login'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh')
]