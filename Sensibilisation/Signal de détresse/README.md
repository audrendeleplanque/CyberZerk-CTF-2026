# Signal de détresse

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Sensibilisation` · **Points** : 100
> **Difficulté** : Intro  
> **Auteur** : Perseval

---

## Description

Marc s'est fait avoir par une attaque en plusieurs temps : un faux fournisseur, un faux technicien, un faux agent de maintenance. Chaque étape a laissé un fragment, encodé différemment. Reconstituez la chaîne pour comprendre l'attaque.

## Fichiers fournis
- chat_support.txt
- mail_fournisseur.txt
- notes_standard.txt

---
 
## Résolution

Dans le fichier `mail_fournisseur.txt` on ce texte : `Q3liZXJaZXJre0NoNDFu`
Une fois décodé en Base64 nous avons : `CyberZerk{Ch41n`

Dans le fichier `notes_standard.txt` on ce texte : `3_1at3a13e13_F0`
Une fois décodé avec le ROT13 nous avons : `3_1ng3n13r13_S0`

Dans le fichier `chat_support.txt` on a ce texte : `6331346c335f4272317333337d`
Une fois décodé de l'Hexadécimal nous avons : `c14l3_Br1s33}`

Une fois assemblé nous avons : `CyberZerk{Ch41n3_1ng3n13r13_S0c14l3_Br1s33}`

---
 
## Flag
 
```
CyberZerk{Ch41n3_1ng3n13r13_S0c14l3_Br1s33}
```