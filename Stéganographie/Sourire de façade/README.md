# Sourire de façade

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Stéganographie` · **Points** : 100
> **Difficulté** : Facile  
> **Auteur** : Perseval

---

## Description

Les RH viennent de publier cette affiche motivationnelle sur le réseau de l'entreprise pour "booster" les développeurs avant la grosse mise en production.

Mais le graphiste, au bord du gouffre, y a discrètement dissimulé son véritable ressenti.

Cherchez au-delà des apparences.

## Fichiers fournis
- motivation.png

---
 
## Résolution

Si on fait un `binwalk` on voit que la signature du fichier correspond à un fichier ZIP. 
Si on ouvre l'image avec 7-zip ça nous donne un fichier texte qui s'appelle `journal_intime.txt` et à l'intérieur nous avons : 

```text
Je n'en peux plus. Ils nous font travailler tous les week-ends sans compensation. Voici la preuve de mon épuisement : CyberZerk{S0ur1r3_P0ur_C4ch3r_L3_Burn0ut}
```

---
 
## Flag
 
```
CyberZerk{S0ur1r3_P0ur_C4ch3r_L3_Burn0ut}
```