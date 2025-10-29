from django.db import models
from django.contrib.auth.models import AbstractUser

# Constantes pour les rôles BTP
ROLE_CHOICES = (
    ('DIR', 'Directeur'),
    ('CDT', 'Conducteur de Travaux'),
    ('RH', 'Ressources Humaines'),
    ('EMP', 'Employé de Chantier'),
    ('ADM', 'Administrateur SaaS'),
)

class CustomUser(AbstractUser):
    # Champ clé pour le Multi-Tenancy (ID de l'entreprise)
    tenant_id = models.CharField(
        max_length=50,
        unique=False, # Un même tenant_id peut avoir plusieurs utilisateurs
        blank=False,
        null=False,
        help_text="Identifiant unique de l'entreprise/client (tenant)."
    )

    # Champ pour le Role-Based Access Control (RBAC)
    role = models.CharField(
        max_length=3,
        choices=ROLE_CHOICES,
        default='EMP',
        help_text="Rôle de l'utilisateur dans l'entreprise (DIR, CDT, RH, etc.)."
    )

    # Ajoutez tout autre champ nécessaire (ex: téléphone, fonction)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # Vous pouvez laisser les autres champs de AbstractUser (username, email, password)
    # tels quels.
    email = models.EmailField(unique=True) # Explicitly define email as unique
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'tenant_id', 'role']

    def __str__(self):
        return f"{self.username} ({self.role} - Tenant: {self.tenant_id})"