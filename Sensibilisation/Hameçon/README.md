# Hameçon 

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Sensibilitation` · **Points** : 50
> **Difficulté** : Facile  
> **Auteur** : Perseval

---

## Description

Marc_V a reçu ce courriel. Sans jamais suivre le lien, dites ce qui cloche — et ce que cache réellement le lien.

## Fichiers fournis
- courriel.eml

---
 
## Résolution

Si on ouvre le mail dans un visualiseur de fichier eml on peut voir ce message : 

```text
Bonjour,

Une anomalie a ete detectee sur votre compte. Pour eviter sa suspension, confirmez vos identifiants sous 24 heures :

https://portail-rh.tricatel.example/securite

Cordialement,
La Direction des Ressources Humaines
```

Si on regarde de plus près le lien on peut voir que ça nous redirige vers : `http://tricatel-rh-verification.xyz/login?id=Q3liZXJaZXJre24zX2NsMXF1M3pfcGFzXzFuc3AzY3Qzel9sM19sMTNufQ`

Si on regarde de plus près le lien nous avons ceci `Q3liZXJaZXJre24zX2NsMXF1M3pfcGFzXzFuc3AzY3Qzel9sM19sMTNufQ` et une fois décodée depuis la Base64 nous avons : `CyberZerk{n3_cl1qu3z_pas_1nsp3ct3z_l3_l13n}`

---
 
## Flag
 
```
CyberZerk{n3_cl1qu3z_pas_1nsp3ct3z_l3_l13n}
```