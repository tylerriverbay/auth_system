from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserLoginView, AdminLoginView, UserListCreateView, UserDetailView
from .views import PermissionViewSet, RoleViewSet
# Defines URL patterns for user and admin login views in a Django application

router = DefaultRouter()
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'permissions', PermissionViewSet, basename='permission')

urlpatterns = [
    path('user/login/', UserLoginView.as_view(), name='user-login'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('', include(router.urls)),
]