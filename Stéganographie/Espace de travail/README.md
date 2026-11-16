# Comparaison Hâtive 

> **CTF** : CyberZerk 2026  
> **Catégorie** : `WEB` · **Points** : 75
> **Difficulté** : Moyen  
> **Auteur** : Perseval

---

## Description

Le portail manager vérifie un code PIN en comparant son md5… un peu vite. ?pin=.

## Liens fournis
- [https://comparaison-hative.cyberzerk.fr](https://comparaison-hative.cyberzerk.fr)

---
 
## Résolution

Dans la première ligne il y a des charactères en mode `Zero Width Space`. 

Une fois extrait nous avons : `z3r0_w1dth_c_3st_pas_vis1bl3`

---
 
## Flag
 
```
CyberZerk{z3r0_w1dth_c_3st_pas_vis1bl3}
```