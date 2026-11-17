# Fragments

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Forensique` · **Points** : 150
> **Difficulté** : Difficile  
> **Auteur** : Perseval

---

## Description

Fragment brut de l'espace non alloué d'un disque, sans table de fichiers. Retrouvez et extrayez ce qui s'y cache.

## Fichiers fournis
- secteur.raw

---
 
## Résolution

Il suffit d'ouvrir le fichier `.raw` avec le bloc note. 
Un `Crtl + F` et on recherche `CyberZerk` et on trouve :

```text
CyberZerk{c4rv1ng_l3_PNG_surv1t_a_l_3ff4c3m3nt}
```

---
 
## Flag
 
```
CyberZerk{c4rv1ng_l3_PNG_surv1t_a_l_3ff4c3m3nt}
```