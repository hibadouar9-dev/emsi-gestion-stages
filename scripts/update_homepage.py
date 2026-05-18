from pathlib import Path

base = '''{% load static %}
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EMSI Stages - {% block title %}{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f8f9ff;
            color: #212529;
        }
        .navbar-brand {
            font-weight: 800;
            font-size: 1.35rem;
        }
        .navbar {
            background: rgba(255,255,255,0.96);
            backdrop-filter: blur(12px);
            box-shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
        }
        .hero-section {
            min-height: 100vh;
            display: flex;
            align-items: center;
            position: relative;
            overflow: hidden;
            background: linear-gradient(135deg, #0d3b9c 0%, #0d6efd 52%, #6f42c1 100%);
            color: white;
        }
        .hero-section::after {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at top left, rgba(255,255,255,0.18), transparent 28%),
                        radial-gradient(circle at bottom right, rgba(255,255,255,0.15), transparent 22%);
            pointer-events: none;
        }
        .hero-card {
            background: rgba(255,255,255,0.95);
            border: 1px solid rgba(255,255,255,0.65);
            box-shadow: 0 25px 60px rgba(16, 41, 77, 0.12);
            backdrop-filter: blur(16px);
        }
        .feature-card, .stats-card, .step-card {
            border: none;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .feature-card:hover, .stats-card:hover, .step-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 24px 60px rgba(44, 84, 212, 0.12);
        }
        .section-title {
            position: relative;
        }
        .section-title::after {
            content: '';
            width: 55px;
            height: 4px;
            background: linear-gradient(90deg, #4f46e5, #0d6efd);
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            bottom: -16px;
            border-radius: 999px;
        }
        footer {
            background: #05132e;
            color: rgba(255,255,255,0.75);
        }
        footer a {
            color: rgba(255,255,255,0.9);
            text-decoration: none;
        }
        .badge-soft-primary {
            background: rgba(56, 103, 214, 0.12);
            color: #1143db;
        }
        .badge-soft-success {
            background: rgba(48, 166, 78, 0.14);
            color: #0f842d;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light sticky-top py-3">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center gap-2" href="{% url 'accueil' %}">
                <img src="{% static 'logo.jpg' %}" alt="Logo EMSI" class="rounded-circle" style="height:42px; width:auto; object-fit:cover; border:2px solid #0d6efd;">
                <span>EMSI Stages</span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto align-items-center">
                    <li class="nav-item mx-1">
                        <a class="nav-link active" href="{% url 'accueil' %}">Accueil</a>
                    </li>
                    <li class="nav-item mx-1">
                        <a class="nav-link" href="#fonctionnalites">Fonctionnalités</a>
                    </li>
                    <li class="nav-item mx-1">
                        <a class="nav-link" href="#comment-ca-marche">Étapes</a>
                    </li>
                    <li class="nav-item mx-1">
                        <a class="nav-link" href="#contact">Contact</a>
                    </li>
                    <li class="nav-item mx-2">
                        <a class="btn btn-primary btn-sm px-4" href="{% url 'connexion' %}">Connexion</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    {% block content %}{% endblock %}

    <footer class="py-5">
        <div class="container">
            <div class="row gy-4">
                <div class="col-md-4">
                    <img src="{% static 'logo.jpg' %}" alt="Logo EMSI" style="height:48px; object-fit:cover;" class="mb-3">
                    <p>Une plateforme moderne pour gérer les conventions de stage, du dépôt jusqu'à la validation.</p>
                </div>
                <div class="col-md-4">
                    <h6 class="text-white mb-3">Liens rapides</h6>
                    <ul class="list-unstyled">
                        <li><a href="{% url 'accueil' %}">Accueil</a></li>
                        <li><a href="{% url 'connexion' %}">Connexion</a></li>
                        <li><a href="{% url 'inscription' %}">Inscription</a></li>
                        <li><a href="#fonctionnalites">Fonctionnalités</a></li>
                    </ul>
                </div>
                <div class="col-md-4" id="contact">
                    <h6 class="text-white mb-3">Contact</h6>
                    <p class="mb-1"><i class="fas fa-envelope me-2"></i>contact@emsi-stages.ma</p>
                    <p><i class="fas fa-phone me-2"></i>+212 6 00 00 00 00</p>
                </div>
            </div>
            <div class="text-center mt-4 text-white-50">
                © 2026 EMSI Stages — Plateforme de gestion de stages
            </div>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>'''

accueil = '''{% extends 'base_accueil.html' %}
{% block title %}Accueil{% endblock %}

{% block content %}
<section class="hero-section">
    <div class="container">
        <div class="row align-items-center gy-5">
            <div class="col-lg-6">
                <span class="badge bg-light text-primary mb-3">Plateforme EMSI — Gestion de stage</span>
                <h1 class="display-5 fw-bold mb-4">Simplifiez le parcours de vos conventions de stage</h1>
                <p class="lead text-white-75 mb-4">Pilotez vos conventions, suivez les validations, retrouvez les offres de stage et centralisez vos échanges en un seul endroit.</p>
                <div class="d-flex flex-column flex-sm-row gap-3">
                    <a href="{% url 'inscription' %}" class="btn btn-light btn-lg px-4 fw-bold">Créer un compte</a>
                    <a href="{% url 'connexion' %}" class="btn btn-outline-light btn-lg px-4 fw-bold">Se connecter</a>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="hero-card p-5 rounded-4">
                    <div class="d-flex align-items-center mb-4">
                        <img src="{% static 'logo.jpg' %}" alt="Logo EMSI" style="height:68px; width:auto; border-radius:18px;">
                        <div class="ms-3">
                            <p class="mb-1 text-muted">EMSI Stages</p>
                            <h4 class="mb-0 fw-bold">Votre outil de stage moderne</h4>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="d-flex justify-content-between mb-2">
                            <span class="text-muted">Conventions gérées</span>
                            <strong>120+</strong>
                        </div>
                        <div class="progress rounded-pill" style="height: 10px;">
                            <div class="progress-bar bg-primary rounded-pill" style="width: 90%;"></div>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="d-flex justify-content-between mb-2">
                            <span class="text-muted">Utilisateurs satisfaits</span>
                            <strong>98%</strong>
                        </div>
                        <div class="progress rounded-pill" style="height: 10px;">
                            <div class="progress-bar bg-success rounded-pill" style="width: 98%;"></div>
                        </div>
                    </div>
                    <div class="mb-3">
                        <div class="d-flex justify-content-between mb-2">
                            <span class="text-muted">Validation rapide</span>
                            <strong>48h</strong>
                        </div>
                        <div class="progress rounded-pill" style="height: 10px;">
                            <div class="progress-bar bg-info rounded-pill" style="width: 85%;"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="py-5 bg-white" id="fonctionnalites">
    <div class="container">
        <div class="text-center mb-5">
            <h2 class="fw-bold section-title">Fonctionnalités clés</h2>
            <p class="text-muted mx-auto" style="max-width:620px;">Un espace unique pour étudiants, tuteurs et services pour gérer toutes les étapes du stage.</p>
        </div>
        <div class="row g-4">
            <div class="col-md-4">
                <div class="feature-card p-4 rounded-4 shadow-sm">
                    <div class="mb-4">
                        <div class="badge bg-primary bg-opacity-10 text-primary rounded-pill py-3 px-3"><i class="fas fa-upload fa-lg"></i></div>
                    </div>
                    <h5 class="fw-bold">Dépôt facile</h5>
                    <p class="text-muted">Importez vos conventions PDF et suivez immédiatement leur dossier.</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="feature-card p-4 rounded-4 shadow-sm">
                    <div class="mb-4">
                        <div class="badge bg-success bg-opacity-10 text-success rounded-pill py-3 px-3"><i class="fas fa-check-circle fa-lg"></i></div>
                    </div>
                    <h5 class="fw-bold">Validation structurée</h5>
                    <p class="text-muted">Validation progressive par tuteur, responsable puis service des stages.</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="feature-card p-4 rounded-4 shadow-sm">
                    <div class="mb-4">
                        <div class="badge bg-info bg-opacity-10 text-info rounded-pill py-3 px-3"><i class="fas fa-briefcase fa-lg"></i></div>
                    </div>
                    <h5 class="fw-bold">Offres intégrées</h5>
                    <p class="text-muted">Découvrez des offres de stage et postulez directement via la plateforme.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="py-5 bg-light">
    <div class="container">
        <div class="text-center mb-5">
            <h2 class="fw-bold section-title">Pourquoi EMSI Stages</h2>
            <p class="text-muted mx-auto" style="max-width:640px;">Une solution pensée pour le monde académique et les acteurs des stages.</p>
        </div>
        <div class="row g-4">
            <div class="col-md-4">
                <div class="p-4 rounded-4 shadow-sm bg-white h-100">
                    <h5 class="fw-bold">100% digital</h5>
                    <p class="text-muted">Plus besoin de papier, tout est centralisé et sécurisé.</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="p-4 rounded-4 shadow-sm bg-white h-100">
                    <h5 class="fw-bold">Suivi en temps réel</h5>
                    <p class="text-muted">Visualisez à tout moment où en est chaque convention.</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="p-4 rounded-4 shadow-sm bg-white h-100">
                    <h5 class="fw-bold">Processus rapide</h5>
                    <p class="text-muted">Réduction significative des délais de validation.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="py-5" id="comment-ca-marche">
    <div class="container">
        <div class="text-center mb-5">
            <h2 class="fw-bold section-title">Comment ça marche ?</h2>
            <p class="text-muted mx-auto" style="max-width:640px;">4 étapes simples pour la création et la validation de votre stage.</p>
        </div>
        <div class="row g-4">
            <div class="col-lg-3 col-sm-6">
                <div class="step-card text-center p-4 rounded-4 bg-white shadow-sm h-100">
                    <div class="step-number mx-auto mb-3">1</div>
                    <h5 class="fw-bold">Inscription</h5>
                    <p class="text-muted small">Créez un compte et commencez votre dossier.</p>
                </div>
            </div>
            <div class="col-lg-3 col-sm-6">
                <div class="step-card text-center p-4 rounded-4 bg-white shadow-sm h-100">
                    <div class="step-number mx-auto mb-3">2</div>
                    <h5 class="fw-bold">Dépôt</h5>
                    <p class="text-muted small">Téléversez votre convention et remplissez les infos.</p>
                </div>
            </div>
            <div class="col-lg-3 col-sm-6">
                <div class="step-card text-center p-4 rounded-4 bg-white shadow-sm h-100">
                    <div class="step-number mx-auto mb-3">3</div>
                    <h5 class="fw-bold">Validation</h5>
                    <p class="text-muted small">Tuteur et responsable examinent votre dossier.</p>
                </div>
            </div>
            <div class="col-lg-3 col-sm-6">
                <div class="step-card text-center p-4 rounded-4 bg-white shadow-sm h-100">
                    <div class="step-number mx-auto mb-3">4</div>
                    <h5 class="fw-bold">Finalisation</h5>
                    <p class="text-muted small">Le service valide la convention et le stage peut démarrer.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="py-5 bg-primary text-white">
    <div class="container text-center">
        <h2 class="fw-bold mb-4">Prêt à démarrer ?</h2>
        <p class="mb-4 fs-5 text-white-75">Rejoignez EMSI Stages et piloter votre convention de bout en bout.</p>
        <a href="{% url 'inscription' %}" class="btn btn-light btn-lg px-5 py-3 fw-bold">Créer mon compte</a>
    </div>
</section>
{% endblock %}'''
Path('templates/stages/accueil.html').write_text(accueil, encoding='utf-8')
"