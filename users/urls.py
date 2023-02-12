from django.urls import path, include
from .views import UserLoginView, UserLogoutView, RegisterUserView, ChangeUserInfoView, AdministrationView, profile

app_name = 'users'
urlpatterns = [
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/logout/', UserLogoutView.as_view(), name='logout'),
    path('accounts/profile/<int:user_id>', profile, name='profile'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('account/profile/change/', ChangeUserInfoView.as_view(), name='change'),
    path('administration/', AdministrationView.as_view(), name='administration'),
    ]

