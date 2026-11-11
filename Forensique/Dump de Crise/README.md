# Dump de Crise

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Forensique` · **Points** : 150
> **Difficulté** : Moyen  
> **Auteur** : Perseval

---

## Description

Voici une copie du dépôt Git de l'intranet Tricatel, récupérée avant le départ d'un dev. Il jure avoir « retiré le secret du code ». Un secret retiré du code n'a pas forcément quitté l'histoire.

## Fichiers fournis
- depot_intranet.tgz

---
 
## Résolution

Si on décompresse le dossier on va se retrouver avec une architecture qui ressemble à un projet destiné à être sur Github.

Si on l'ouvre dans VSCode et qu'on regarde dans l'historique des pushs nous pouvons voir qu'il y a un push appelé : `Ajout script de déploiement`

Dans ce dernier on trouve : `API_KEY="CyberZerk{G1t_N0ubl13_J4m41s_R13n_Du_P4ss3}"`

---
 
## Flag
 
```
CyberZerk{G1t_N0ubl13_J4m41s_R13n_Du_P4ss3}
```