# Le Chiffrement Militaire

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Cryptographie` · **Points** : 100
> **Difficulté** : Intro  
> **Auteur** : Perseval

---

## Description

Le service IT de Tricatel a réinitialisé vos accès suite à votre arrêt maladie.

Ils affirment avoir utilisé un "algorithme de chiffrement militaire à triple couche" pour sécuriser votre mot de passe temporaire.

À vue de nez, ça ressemble surtout à un encodage classique répété pour faire illusion...

Voici votre token : VVROc2FWcFlTbUZhV0VweVpUQkpNR042VFRKT1JqbFBUVE5PTUZneFFUQmpNVGxGWkZZNVJHRkVSbTFhYmtsNllsUk9kV1JJTUQwPQ==

---
 
## Résolution

Dans l'énoncé on peut trouver : `VVROc2FWcFlTbUZhV0VweVpUQkpNR042VFRKT1JqbFBUVE5PTUZneFFUQmpNVGxGWkZZNVJHRkVSbTFhYmtsNllsUk9kV1JJTUQwPQ==`

Après trois couche de décodage en Base64 nous avons : `CyberZerk{B4s364_N3st_P4s_Du_Ch1ffr3m3nt}`

---
 
## Flag
 
```
CyberZerk{B4s364_N3st_P4s_Du_Ch1ffr3m3nt}
```