# core_auth/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Importez votre CustomUser


# Remarquez que nous héritons de UserAdmin pour obtenir toutes les fonctionnalités de base de l'utilisateur
class CustomUserAdmin(UserAdmin):
    # Les champs à afficher dans la liste (Tenant ID et Role sont ajoutés)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'tenant_id', 'role')

    # Les champs que vous voulez pouvoir modifier
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Informations SaaS', {'fields': ('tenant_id', 'role')}),  # Votre section custom
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Ajoutez les champs custom aux champs de recherche et aux filtres
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'tenant_id', 'role')
    search_fields = ('username', 'email', 'tenant_id')


# Désenregistrez le modèle User par défaut (si vous ne l'utilisez plus) et enregistrez le CustomUser
admin.site.register(CustomUser, CustomUserAdmin)

# Si vous avez utilisé le modèle User par défaut au départ et que vous avez des erreurs, vous pouvez essayer de désenregistrer la classe User par défaut
# try:
#     from django.contrib.auth.models import User
#     admin.site.unregister(User)
# except admin.sites.NotRegistered:
#     pass