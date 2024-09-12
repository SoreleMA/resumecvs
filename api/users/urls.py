from django.urls import path
from .views import UserListCreateAPIView, UserDetailAPIView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:id>/', UserDetailAPIView.as_view(), name='user-detail'),
]