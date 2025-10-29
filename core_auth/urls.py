
from django.urls import path
from .views import RegisterView, ProtectedView, RequestPasswordResetEmailView, SetNewPasswordView



urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('protected-test/', ProtectedView.as_view(), name='protected_test'),
    path('request-reset-email/', RequestPasswordResetEmailView.as_view(), name="request-reset-email"),
    path('password-reset-confirm/<uidb64>/<token>/', SetNewPasswordView.as_view(), name="password-reset-confirm"),
]