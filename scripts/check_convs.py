from stages.models import Convention, Evaluation, Utilisateur
import datetime

today = datetime.date.today()
print('TODAY:', today)

tutors = Utilisateur.objects.filter(role='tuteur')
print('TUTEURS:', list(tutors.values_list('username', flat=True)))

convs = Convention.objects.filter(statut='validee')
print('CONVS count:', convs.count())

for c in convs:
    try:
        e = c.evaluation
        eval_exists = True
    except Exception:
        eval_exists = False
    print('ID', c.id, 'etudiant', c.etudiant.username, 'date_fin', c.date_fin, 'finished?', c.date_fin < today, 'has_eval', eval_exists)
