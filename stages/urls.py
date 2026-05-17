from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('connexion/', views.connexion, name='connexion'),  # ← Ajoutez le chemin
    path('inscription/', views.inscription, name='inscription'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('depot/', views.depot_convention, name='depot_convention'),
    path('mes-conventions/', views.mes_conventions, name='mes_conventions'),
    path('a-valider/', views.conventions_a_valider, name='conventions_a_valider'),
    path('valider/<int:convention_id>/', views.valider_convention, name='valider_convention'),
    path('refuser/<int:convention_id>/', views.refuser_convention, name='refuser_convention'),
    path('service/offres/', views.liste_offres_service, name='liste_offres_service'),
    path('service/offres/creer/', views.creer_offre, name='creer_offre'),
    path('service/offres/modifier/<int:offre_id>/', views.modifier_offre, name='modifier_offre'),
    path('service/offres/supprimer/<int:offre_id>/', views.supprimer_offre, name='supprimer_offre'),
    path('offres/', views.consulter_offres, name='consulter_offres'),
    path('offres/postuler/<int:offre_id>/', views.postuler_offre, name='postuler_offre'),
    path('mes-candidatures/', views.mes_candidatures, name='mes_candidatures'),
    path('service/candidatures/', views.gerer_candidatures, name='gerer_candidatures'),
    path('service/candidatures/<int:candidature_id>/<str:statut>/', views.modifier_statut_candidature, name='modifier_statut_candidature'),
]