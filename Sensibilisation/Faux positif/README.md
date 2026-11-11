# Faux Positif

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Sensibilisation` · **Points** : 62
> **Difficulté** : Facile  
> **Auteur** : Perseval

---

## Description

Quatre mails sont arrivés dans la boîte de l'équipe. Un seul ne vient pas vraiment de Tricatel. Repérez le phishing à ses en-têtes ; son identifiant de suivi dira le reste.

## Fichiers fournis
- boite_reception.txt

---
 
## Résolution

A la fin du fichier on peut lire : 

```
Indice : un seul de ces mails ne vient pas vraiment de Tricatel.
Son identifiant de suivi en dit long.
```

Dans le fichier on peut trouver : `Q3liZXJaZXJre1VuX0Iwbl9SM2ZsM3gzX1VuX0NsMWNfRXYxdDN9` en tant que X-Tracking-Id

En le mettant dans CyberChef on trouve : `CyberZerk{Un_B0n_R3fl3x3_Un_Cl1c_Ev1t3}`. C'était en Base64. 

---
 
## Flag
 
```
CyberZerk{Un_B0n_R3fl3x3_Un_Cl1c_Ev1t3}
```