from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .serializers import UserLoginSerializer, AdminLoginSerializer
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import UserSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly

class UserLoginView(APIView):
    '''Validates regular user login and returns auth token if active and user'''
    @extend_schema(
        request=UserLoginSerializer,
        responses={200: UserLoginSerializer},
        tags=["user"]
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class AdminLoginView(APIView):
    '''Validates admin login and returns auth token if active and admin'''
    @extend_schema(
        request=AdminLoginSerializer,
        responses={200: AdminLoginSerializer},
        tags=["admin"]
    )
    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    
class UserListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    @extend_schema(request=UserSerializer, responses=UserSerializer)
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @extend_schema(request=UserSerializer, responses=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    
    @extend_schema(responses=UserSerializer)
    def get(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @extend_schema(request=UserSerializer, responses=UserSerializer)
    def put(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
from rest_framework import viewsets
from .models import Role
from .serializers import RoleSerializer
    
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdminOrReadOnly]

from django.contrib.auth.models import Permission
from .serializers import PermissionSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAdminOrReadOnly]