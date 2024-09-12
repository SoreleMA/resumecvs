from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                refresh = RefreshToken.for_user(user)
                response_data = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'role': user.role,
                    'email': user.email,
                }

                # Verificar el rol del usuario y retornar una respuesta adecuada
                if user.role == 'admin':
                    response_data['message'] = 'Logged in as administrator'
                elif user.role == 'user':
                    response_data['message'] = 'Logged in as client'
                elif user.role == 'company':
                    response_data['message'] = 'Logged in as company'

                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Account is inactive'}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users= User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetailAPIView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_user(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request,id):
        user = self.get_user(id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)    
    
    def put(self, request, id):
        user = self.get_user(id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        user = self.get_user(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

