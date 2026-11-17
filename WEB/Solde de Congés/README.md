# Solde de Congés

> **CTF** : CyberZerk 2026  
> **Catégorie** : `WEB` · **Points** : 212
> **Difficulté** : Difficile  
> **Auteur** : Perseval

---

## Description

POST /start (solde = 1 jour) ; POST /book consomme ; GET /flag. Passez le solde négatif.

## Liens fournis
- [https://solde-conges.cyberzerk.fr](https://solde-conges.cyberzerk.fr)

## Fichiers fournis
- CONNEXION.txt

---
 
## Résolution

On sait que le serveur vérifie puis décrément le solde. Donc on va envoyé 10 demandes sur la requête `/book` et nous pouvons accéder au flag. 

Le fichier `script.py` fonctionne si vous voulez en savoir plus. 

---
 
## Flag
 
```
CyberZerk{PHP_uns3r1al1z3_p0p_ch41n_v14_w4k3up}
```