from rest_framework.views import APIView
from rest_framework import status, authentication, permissions, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from users.serializers import RegisterSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

@authentication_classes([authentication.TokenAuthentication, authentication.SessionAuthentication, authentication.BasicAuthentication])
@permission_classes([permissions.IsAuthenticated])
class LogoutView(APIView):

    def get(self, request):
        # Perform the logout action, such as invalidating the session or token
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)