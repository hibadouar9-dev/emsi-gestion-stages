from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import OffreStage, Utilisateur, Convention

class InscriptionForm(UserCreationForm):
    campus = forms.ChoiceField(choices=[('Casablanca', 'Casablanca'), ('Rabat', 'Rabat'), ('Tanger', 'Tanger'), ('Marrakech', 'Marrakech'), ('Fès', 'Fès')])
    filiere = forms.ChoiceField(choices=[('GI', 'GI'), ('GE', 'GE'), ('IIA', 'IIA'), ('GINF', 'GINF')])
    
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'first_name', 'last_name', 'campus', 'filiere', 'password1', 'password2']

class ConnexionForm(AuthenticationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'password']

class ConventionForm(forms.ModelForm):
    class Meta:
        model = Convention
        fields = ['entreprise_nom', 'entreprise_adresse', 'tuteur_entreprise_nom', 
                  'tuteur_entreprise_email', 'tuteur_entreprise_telephone',
                  'date_debut', 'date_fin', 'mission', 'convention_originale']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'mission': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'entreprise_nom': forms.TextInput(attrs={'class': 'form-control'}),
            'entreprise_adresse': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'tuteur_entreprise_nom': forms.TextInput(attrs={'class': 'form-control'}),
            'tuteur_entreprise_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'tuteur_entreprise_telephone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OffreStageForm(forms.ModelForm):
    class Meta:
        model = OffreStage
        fields = ['titre', 'description', 'lieu', 'duree', 'date_limite', 'active']
        widgets = {
            'date_limite': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'duree': forms.TextInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }