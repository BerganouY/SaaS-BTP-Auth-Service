from django.urls import path
from .template_views import (
    LoginTemplateView,
    RegisterTemplateView,
    ProtectedTestTemplateView,
    RequestPasswordResetEmailTemplateView,
    PasswordResetConfirmTemplateView,
)

urlpatterns = [
    path('login/', LoginTemplateView.as_view(), name='login'),
    path('register/', RegisterTemplateView.as_view(), name='register'),
    path('protected-test/', ProtectedTestTemplateView.as_view(), name='protected_test_template'),
    path('request-password-reset/', RequestPasswordResetEmailTemplateView.as_view(), name='request_password_reset'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmTemplateView.as_view(), name='password_reset_confirm_template'),
]
