# L'SQL ou la cuisse ?

> **CTF** : CyberZerk 2026  
> **Catégorie** : `WEB` · **Points** : 100
> **Difficulté** : Intro  
> **Auteur** : Perseval

---

## Description

Le développeur principal de la startup Tricatel-Cyber vient de faire un burn-out sévère. Sous la pression de livrer le nouveau portail RH, il a codé le système d'authentification à 4h du matin après trois nuits blanches consécutives, en ingérant un mélange toxique de caféine et de stress.

Le code est bâclé. La santé mentale de l'équipe est en danger.

Connectez-vous en tant qu'administrateur pour récupérer la note interne confidentielle du PDG et prouvez que le système est défaillant.

## Liens fournis
- [http://sql.cyberzerk.fr](https://sql.cyberzerk.fr)

---
 
## Résolution

On tombe sur interface de connexion. 

Le nom du challenge nous met sur une piste, SQL. 

Essayons une injection SQL basique avec `' OR 1=1 --` en tant que mot de passe et `admin` en tant que nom d'utilisateur. 

Cela fonctionne et nous avons : 

```text
[+] Connexion réussie.

Bienvenue l'équipe RH. Prêts à faire chier les devs aujourd'hui ? N'oubliez pas de leur rappeler de remplir leurs feuilles de temps.

>> Memo_Direction.txt
"L'équipe de dev est à bout. On ne remplace personne, offrez-leur juste un baby-foot et rappelez-leur qu'on est une famille pour compenser les 60h/semaine. S'ils craquent, c'est qu'ils ne sont pas faits pour la cyber."

CyberZerk{SQL_1nj3ct10n_C4us3d_By_Burn0ut}
```

---
 
## Flag
 
```
CyberZerk{SQL_1nj3ct10n_C4us3d_By_Burn0ut}
```