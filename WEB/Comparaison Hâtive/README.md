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

On peut voir sur le site ce texte : 

```text
// Portail d'acces rapide manager, protege par code PIN.
// Note: PIN admin a 6 chiffres, je l'ai mis en dur. Pas le temps de faire propre, je verrai lundi.
```

Donc nous allons voir le code source de la page. En haut nous avons cette ligne : 

```text
<!-- TODO Didier: virer la sauvegarde config.php.bak avant la prod, elle traine a la racine. -->
```

Donc nous allons pouvoir accéder à ce lien : [https://comparaison-hative.cyberzerk.fr/config.php.bak](https://comparaison-hative.cyberzerk.fr/config.php.bak)

Ce texte apparait : 

```text
<?php
// Configuration portail manager Tricatel.
$PIN_HASH = "1a31076f2aeb1e7d69120c9f85c3a8da"; // md5 du PIN admin (6 chiffres)
```

Si nous décodons le `MD5` fourni nous avons : `496135`

Donc maintenant prenons ce code et mettons le dans le site de base. 

Et le flag suivant apparait : `CyberZerk{un3_sauv3g4rd3_.bak_tr4h1t_l3_pin}`

---
 
## Flag
 
```
CyberZerk{un3_sauv3g4rd3_.bak_tr4h1t_l3_pin}
```