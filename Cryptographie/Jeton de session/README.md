# Le Jeton de Session

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Cryptographie` · **Points** : 296
> **Difficulté** : Difficile  
> **Auteur** : Perseval

---

## Description

Les jetons de session sont tirés avec getrandbits(32). 624 jetons consécutifs ont fuité (tokens.txt). La note du DRH (secret.bin) est chiffrée par XOR avec les octets des jetons SUIVANTS.

## Fichiers fournis
- tokens.txt
- secret.bin

---
 
## Résolution

Le fichier tokens.txt contient 624 jetons consécutifs générés avec getrandbits(32). Or, le générateur MT19937 utilisé par Python possède un état interne de 624 mots de 32 bits. En inversant les opérations de tempering appliquées aux sorties (untempering), il est donc possible de reconstruire cet état interne.

J'ai ensuite restauré le générateur avec cet état afin de prédire les jetons suivants. Ces derniers ont servi à reconstituer le flux d'octets utilisé comme clé XOR pour déchiffrer secret.bin.

Cette attaque permet de retrouver la note du DRH sans connaître la clé initiale, simplement à partir des 624 jetons ayant fuité.

---
 
## Flag
 
```
CyberZerk{MT19937_s3_cl0n3_av3c_624_s0rt13s_untemper}
```