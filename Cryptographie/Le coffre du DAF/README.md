# Le Coffre du DAF

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Cryptographie` · **Points** : 100
> **Difficulté** : Moyen  
> **Auteur** : Perseval

---

## Description

Le DAF a « chiffré » le contenu de son coffre avec un petit script maison. On a récupéré le résultat en hexadécimal. Il paraît qu'il réutilise toujours la même clé, encore et encore.

## Fichiers fournis
- coffre_chiffre.hex

---
 
## Résolution

Dans le fichier on peut trouver le texte suivant : `172b2b26330e203e3f291173130b177f24613d701e171a7f2726161375271a1f67313c3170277631`

L'algorithme utilisé c'est le XOR répétitif avec la clé `TRICATEL`, une fois décodé nous avons : `CyberZerk{X0R_R3p3t3_C_3st_P4s_S3cur1s3}`

---
 
## Flag
 
```
CyberZerk{X0R_R3p3t3_C_3st_P4s_S3cur1s3}
```