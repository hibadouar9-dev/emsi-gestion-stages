from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import InscriptionForm, ConnexionForm

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'etudiant'
            user.save()
            login(request, user)
            messages.success(request, f'Bienvenue {user.username} ! Votre compte est créé.')
            return redirect('dashboard')
    else:
        form = InscriptionForm()
    return render(request, 'stages/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bonjour {user.username} !')
                return redirect('dashboard')
        messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = ConnexionForm()
    return render(request, 'stages/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    messages.info(request, 'Vous êtes déconnecté.')
    return redirect('connexion')

@login_required
def dashboard(request):
    return render(request, 'stages/dashboard.html', {'user': request.user})

from .forms import ConventionForm
from .models import Convention

@login_required
def depot_convention(request):
    if request.user.role != 'etudiant':
        messages.error(request, 'Seuls les étudiants peuvent déposer une convention.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = ConventionForm(request.POST, request.FILES)
        if form.is_valid():
            convention = form.save(commit=False)
            convention.etudiant = request.user
            convention.save()
            messages.success(request, '✅ Convention déposée avec succès ! En attente de validation.')
            return redirect('mes_conventions')
        else:
            messages.error(request, '❌ Erreur dans le formulaire. Vérifiez les champs.')
    else:
        form = ConventionForm()
    
    return render(request, 'stages/depot_convention.html', {'form': form})

@login_required
def mes_conventions(request):
    if request.user.role != 'etudiant':
        return redirect('dashboard')
    
    conventions = Convention.objects.filter(etudiant=request.user).order_by('-date_depot')
    return render(request, 'stages/mes_conventions.html', {'conventions': conventions})

@login_required
def conventions_a_valider(request):
    user = request.user
    if user.role == 'tuteur':
        conventions = Convention.objects.filter(statut='attente_tuteur')
    elif user.role == 'responsable':
        conventions = Convention.objects.filter(statut='attente_responsable')
    elif user.role == 'service':
        conventions = Convention.objects.filter(statut='attente_service')
    else:
        messages.error(request, 'Vous n\'avez pas accès à cette page')
        return redirect('dashboard')
    
    return render(request, 'stages/conventions_a_valider.html', {'conventions': conventions})

@login_required
def valider_convention(request, convention_id):
    convention = get_object_or_404(Convention, id=convention_id)
    user = request.user
    
    if user.role == 'tuteur' and convention.statut == 'attente_tuteur':
        convention.statut = 'attente_responsable'
        convention.save()
        messages.success(request, f'✅ Convention validée. Transmise au responsable.')
    elif user.role == 'responsable' and convention.statut == 'attente_responsable':
        convention.statut = 'attente_service'
        convention.save()
        messages.success(request, f'✅ Convention validée. Transmise au service des stages.')
    elif user.role == 'service' and convention.statut == 'attente_service':
        convention.statut = 'validee'
        convention.save()
        messages.success(request, f'✅ Convention validée définitivement !')
    else:
        messages.error(request, '❌ Vous ne pouvez pas valider cette convention')
    
    return redirect('conventions_a_valider')

@login_required
def refuser_convention(request, convention_id):
    convention = get_object_or_404(Convention, id=convention_id)
    
    if request.method == 'POST':
        commentaire = request.POST.get('commentaire', '')
        convention.statut = 'refusee'
        convention.commentaire_refus = commentaire
        convention.save()
        messages.warning(request, f'❌ Convention refusée : {commentaire}')
        return redirect('conventions_a_valider')
    
    return render(request, 'stages/refuser_convention.html', {'convention': convention})

from .models import OffreStage
from .forms import OffreStageForm

# === GESTION DES OFFRES (SERVICE STAGES) ===
@login_required
def liste_offres_service(request):
    if request.user.role != 'service':
        messages.error(request, 'Accès non autorisé')
        return redirect('dashboard')
    
    offres = OffreStage.objects.all().order_by('-date_creation')
    return render(request, 'stages/service_offres.html', {'offres': offres})

@login_required
def creer_offre(request):
    if request.user.role != 'service':
        messages.error(request, 'Accès non autorisé')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = OffreStageForm(request.POST)
        if form.is_valid():
            offre = form.save(commit=False)
            offre.entreprise = request.user
            offre.save()
            messages.success(request, f'✅ Offre "{offre.titre}" créée avec succès !')
            return redirect('liste_offres_service')
        else:
            messages.error(request, 'Erreur dans le formulaire')
    else:
        form = OffreStageForm()
    
    return render(request, 'stages/creer_offre.html', {'form': form})

@login_required
def modifier_offre(request, offre_id):
    if request.user.role != 'service':
        messages.error(request, 'Accès non autorisé')
        return redirect('dashboard')
    
    offre = get_object_or_404(OffreStage, id=offre_id)
    
    if request.method == 'POST':
        form = OffreStageForm(request.POST, instance=offre)
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ Offre "{offre.titre}" modifiée avec succès !')
            return redirect('liste_offres_service')
    else:
        form = OffreStageForm(instance=offre)
    
    return render(request, 'stages/modifier_offre.html', {'form': form, 'offre': offre})

@login_required
def supprimer_offre(request, offre_id):
    if request.user.role != 'service':
        messages.error(request, 'Accès non autorisé')
        return redirect('dashboard')
    
    offre = get_object_or_404(OffreStage, id=offre_id)
    
    if request.method == 'POST':
        titre = offre.titre
        offre.delete()
        messages.success(request, f'✅ Offre "{titre}" supprimée avec succès !')
        return redirect('liste_offres_service')
    
    return render(request, 'stages/supprimer_offre.html', {'offre': offre})

# === CONSULTATION DES OFFRES (ETUDIANTS) ===
@login_required
def consulter_offres(request):
    if request.user.role != 'etudiant':
        messages.error(request, 'Accès non autorisé')
        return redirect('dashboard')
    
    offres = OffreStage.objects.filter(active=True).order_by('-date_creation')
    return render(request, 'stages/consulter_offres.html', {'offres': offres})

from .models import Candidature

@login_required
def postuler_offre(request, offre_id):
    if request.user.role != 'etudiant':
        messages.error(request, 'Seuls les étudiants peuvent postuler')
        return redirect('dashboard')
    
    offre = get_object_or_404(OffreStage, id=offre_id, active=True)
    
    # Vérifier si l'étudiant a déjà postulé
    deja_postule = Candidature.objects.filter(etudiant=request.user, offre=offre).exists()
    
    if request.method == 'POST':
        if deja_postule:
            messages.warning(request, 'Vous avez déjà postulé à cette offre')
        else:
            message = request.POST.get('message', '')
            Candidature.objects.create(
                etudiant=request.user,
                offre=offre,
                message=message
            )
            messages.success(request, f'✅ Candidature envoyée pour "{offre.titre}"')
        return redirect('consulter_offres')
    
    return render(request, 'stages/postuler_offre.html', {'offre': offre, 'deja_postule': deja_postule})

@login_required
def mes_candidatures(request):
    if request.user.role != 'etudiant':
        return redirect('dashboard')
    
    candidatures = Candidature.objects.filter(etudiant=request.user).order_by('-date_candidature')
    return render(request, 'stages/mes_candidatures.html', {'candidatures': candidatures})

@login_required
def gerer_candidatures(request):
    if request.user.role != 'service':
        messages.error(request, 'Accès non autorisé')
        return redirect('dashboard')
    
    candidatures = Candidature.objects.all().order_by('-date_candidature')
    return render(request, 'stages/gerer_candidatures.html', {'candidatures': candidatures})

@login_required
def modifier_statut_candidature(request, candidature_id, statut):
    if request.user.role != 'service':
        messages.error(request, 'Accès non autorisé')
        return redirect('dashboard')
    
    candidature = get_object_or_404(Candidature, id=candidature_id)
    if statut in ['acceptee', 'refusee']:
        candidature.statut = statut
        candidature.save()
        messages.success(request, f'Candidature {statut} pour {candidature.etudiant.username}')
    
    return redirect('gerer_candidatures')

def accueil(request):
    return render(request, 'stages/accueil.html')