from django.views.generic import TemplateView

class LoginTemplateView(TemplateView):
    template_name = 'core_auth/login.html'

class RegisterTemplateView(TemplateView):
    template_name = 'core_auth/register.html'

class ProtectedTestTemplateView(TemplateView):
    template_name = 'core_auth/protected_test.html'

class RequestPasswordResetEmailTemplateView(TemplateView):
    template_name = 'core_auth/request_reset_email.html'

class PasswordResetConfirmTemplateView(TemplateView):
    template_name = 'core_auth/password_reset_confirm.html'
