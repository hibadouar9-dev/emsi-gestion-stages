from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Candidature, Evaluation, OffreStage, Utilisateur, Convention

class UtilisateurAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'campus', 'filiere')
    list_filter = ('role', 'campus')
    fieldsets = UserAdmin.fieldsets + (
        ('Informations EMSI', {'fields': ('role', 'campus', 'filiere', 'telephone')}),
    )

admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(Convention)
admin.site.register(OffreStage)
admin.site.register(Evaluation)
admin.site.register(Candidature)