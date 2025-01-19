from django.urls import path
from .views import RegisterUserView, LoginUserView, UserProfileUpdateView, PasswordChangeView,SendOTPView, ResetPasswordView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path('login/', LoginUserView.as_view(), name='user-login'),  # Login URL
    path('update/', UserProfileUpdateView.as_view(), name='user-update'), 
    path('change-password/', PasswordChangeView.as_view(), name='password-change'),
    path('send-otp/', SendOTPView.as_view(), name='send-otp'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]
