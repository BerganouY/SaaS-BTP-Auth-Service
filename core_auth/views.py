from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model

from .models import CustomUser
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
class ProtectedView(APIView):
    # CLÉ : Seuls les utilisateurs avec un token JWT valide peuvent y accéder
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # request.user est automatiquement renseigné par le JWTAuthentication
        return Response({
            "message": f"Accès réussi. Bienvenue {request.user.username}!",
            "user_id": request.user.id,
            "tenant_id": request.user.tenant_id,
            "role": request.user.role
        })

from rest_framework import status
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str, DjangoUnicodeDecodeError, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from .serializers import PasswordResetRequestSerializer, SetNewPasswordSerializer

class RequestPasswordResetEmailView(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)

            # Construct the reset link (this should be your frontend URL)
            # For testing, we'll just print it or use a placeholder
            reset_link = f"{request.scheme}://{request.get_host()}/auth/password-reset-confirm/{uidb64}/{token}"

            email_body = render_to_string('email/password_reset.html', {
                'user': user,
                'reset_link': reset_link,
            })

            email_subject = 'Password Reset Request'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]

            email_message = EmailMessage(email_subject, email_body, email_from, recipient_list)
            email_message.content_subtype = "html" # Main content is now HTML
            email_message.send()

            return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        return Response({'error': 'User with provided email does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, uidb64, token):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data['password']

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist, DjangoUnicodeDecodeError):
            user = None

        if user is not None and PasswordResetTokenGenerator().check_token(user, token):
            user.set_password(password)
            user.save()
            return Response({'success': 'Password reset successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)