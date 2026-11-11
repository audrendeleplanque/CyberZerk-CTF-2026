# Arrêt Maladie

> **CTF** : CyberZerk 2026  
> **Catégorie** : `WEB` · **Points** : 100
> **Difficulté** : Intro  
> **Auteur** : Perseval

---

## Description

Le portail des absences est en ligne.

Vous avez accès à votre propre dossier de demande de congés.

Un collègue a posé un arrêt maladie hier suite à une pression insoutenable de la direction, son dossier doit se trouver juste avant le vôtre.

Trouvez un moyen de lire son rapport d'absence.

## Liens fournis
- [https://absences.cyberzerk.fr](https://absences.cyberzerk.fr)

---
 
## Résolution

On peut voir que les numéros de dossiers sont passé dans les paramètres de l'URL. 

Nous avons ce lien : `https://absences.cyberzerk.fr/?dossier_id=1042`

Si nous essayons d'atteindre ce lien : `https://absences.cyberzerk.fr/?dossier_id=1041`

Nous avons ceci : 

```text
Utilisateur authentifié : Employé #8472 (Droits standards)

Strictement Confidentiel - Secret Médical
Dossier #1041 - Arrêt Maladie Prolongé
Employé : Marc V. (Développeur Senior)

Rapport Médecine du Travail : Épuisement professionnel sévère (Burn-out). Le patient décrit des horaires de 70h/semaine, un isolement total et un harcèlement moral de la direction ("Vous êtes remplaçable en un claquement de doigts").

Action RH recommandée : Contester l'arrêt maladie et bloquer les accès informatiques du collaborateur pour éviter toute fuite de données.

CyberZerk{ID0R_M4n4g3m3nt_T0x1qu3}
```

---
 
## Flag
 
```
CyberZerk{ID0R_M4n4g3m3nt_T0x1qu3}
```