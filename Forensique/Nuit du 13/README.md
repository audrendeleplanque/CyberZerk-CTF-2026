# Nuit du 13

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Forensique` · **Points** : 75
> **Difficulté** : Moyen  
> **Auteur** : Perseval

---

## Description

Dans la nuit du 13 novembre, un fichier confidentiel a quitté l'intranet de Tricatel. Voici le journal d'accès du serveur. Retrouvez la requête d'exfiltration qui a réussi.

## Fichiers fournis
- access.log

---
 
## Résolution

Dans le fichier on va chercher une requête `GET` qui a pour code `200`. 
On peut voir qu'à `13/Nov/2026:02:47:03 +0100` nous avons cette ligne : `[13/Nov/2026:02:47:03 +0100] "GET /export.php?file=rapport_confidentiel_rh.zip&token=CyberZerk%7BL0g_4n4lys3_Exf1l_C0nf1rm33%7D HTTP/1.1" 200 184320 "-" "curl/8.2.1"`

On peut voir que le token de la requête est : `CyberZerk%7BL0g_4n4lys3_Exf1l_C0nf1rm33%7D`
Une fois décodé en URL cela donne : `CyberZerk{L0g_4n4lys3_Exf1l_C0nf1rm33}`

---
 
## Flag
 
```
CyberZerk{L0g_4n4lys3_Exf1l_C0nf1rm33}
```