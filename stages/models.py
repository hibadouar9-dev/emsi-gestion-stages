from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator

class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ('etudiant', 'Étudiant'),
        ('tuteur', 'Tuteur pédagogique'),
        ('responsable', 'Responsable de filière'),
        ('service', 'Service des stages'),
        ('entreprise', 'Entreprise'),
        ('admin', 'Administrateur'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='etudiant')
    campus = models.CharField(max_length=50, blank=True, null=True)
    filiere = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class Convention(models.Model):
    STATUT_CHOICES = [
        ('attente_tuteur', '📋 En attente tuteur'),
        ('attente_responsable', '👨‍🏫 En attente responsable'),
        ('attente_service', '📄 En attente service'),
        ('validee', '✅ Validée'),
        ('refusee', '❌ Refusée'),
    ]
    
    etudiant = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='conventions')
    
    # Informations entreprise
    entreprise_nom = models.CharField(max_length=200)
    entreprise_adresse = models.TextField(blank=True)
    tuteur_entreprise_nom = models.CharField(max_length=200)
    tuteur_entreprise_email = models.EmailField()
    tuteur_entreprise_telephone = models.CharField(max_length=20)
    
    # Dates et mission
    date_debut = models.DateField()
    date_fin = models.DateField()
    mission = models.TextField()
    
    # Fichier
    convention_originale = models.FileField(
        upload_to='conventions/',
        validators=[FileExtensionValidator(['pdf'])],
        verbose_name="Convention signée (PDF)"
    )
    
    # Suivi
    statut = models.CharField(max_length=30, choices=STATUT_CHOICES, default='attente_tuteur')
    commentaire_refus = models.TextField(blank=True)
    date_depot = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.etudiant.username} - {self.entreprise_nom} ({self.get_statut_display()})"

class OffreStage(models.Model):
    entreprise = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='offres')
    titre = models.CharField(max_length=200)
    description = models.TextField()
    lieu = models.CharField(max_length=200)
    duree = models.CharField(max_length=100)
    date_limite = models.DateField()
    active = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre

class Evaluation(models.Model):
    convention = models.OneToOneField(Convention, on_delete=models.CASCADE, related_name='evaluation')
    note_tuteur_emsi = models.IntegerField(null=True, blank=True)
    commentaire_tuteur_emsi = models.TextField(blank=True)
    date_evaluation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Évaluation {self.convention.id} - {self.note_tuteur_emsi}/20"
    
class Candidature(models.Model):
    STATUT_CHOICES = [
        ('en_attente', '⏳ En attente'),
        ('acceptee', '✅ Acceptée'),
        ('refusee', '❌ Refusée'),
    ]
    
    etudiant = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='candidatures')
    offre = models.ForeignKey(OffreStage, on_delete=models.CASCADE, related_name='candidatures')
    message = models.TextField(blank=True, help_text="Lettre de motivation ou message")
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    date_candidature = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['etudiant', 'offre']  # Un étudiant ne peut postuler qu'une fois par offre
        ordering = ['-date_candidature']
    
    def __str__(self):
        return f"{self.etudiant.username} → {self.offre.titre} ({self.get_statut_display()})"