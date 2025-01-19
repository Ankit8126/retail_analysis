from django.urls import path
from .views import RegisterUserView, LoginUserView, UserProfileUpdateView, PasswordChangeView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-register'),
    path('login/', LoginUserView.as_view(), name='user-login'),  # Login URL
    path('update/', UserProfileUpdateView.as_view(), name='user-update'), 
    path('change-password/', PasswordChangeView.as_view(), name='password-change'),
]
