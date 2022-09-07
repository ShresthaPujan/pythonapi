from django.urls import path
from account.views import SendPasswordResetEmailView, UserChangePasswordView, UserRegistrationView , UserLoginView,UserProfileView, UserpasswordResetView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('userprofile/',UserProfileView.as_view(), name='userprofile'),
    path('changepassword/',UserChangePasswordView.as_view(), name='changepassword'),
    path('passwordreset/',SendPasswordResetEmailView.as_view(), name='passwordreset'),
    path('reset-password/<uid>/<token>/',UserpasswordResetView.as_view(), name='reset-password'),
]