from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User

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


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        data = request.data
        if User.objects.filter(username=data['username']).exists():
            return Response({'error': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=data['username'], password=data['password'])
        return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)



