from rest_framework.views import APIView
from rest_framework import status, authentication, permissions, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt import authentication
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import Account
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import  UserSerializer, RegisterSerializer, LoginSerializer

#create JWT login class with method post

@permission_classes([AllowAny])
class RegistrationView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([authentication.JWTAuthentication])
@permission_classes([AllowAny, ])
class LoginView(APIView):
    def post(self, request):
        print(f"----- {request.data}")
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        user = User.objects.get(username=username)
        if user:
            print(login(request, user))
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({
            'user_id': user.pk,
            'username': user.username,
            'token': str(refresh.access_token),
            'refresh_token': str(refresh)
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=400)


@authentication_classes([authentication.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
class LogoutView(APIView):
    def post(self, request):
        print("logout")
        try:
            print(request.data['username'])
            user = User.objects.get(username=request.data['username'])
            # logout(user)
        
            token = RefreshToken.for_user(user)
            token.blacklist()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(owner=instance, name=f"{instance.username}")