# La Voix Intérieure

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Cryptographie` · **Points** : 100
> **Difficulté** : Intro  
> **Auteur** : Perseval

---

## Description

Le DAF chiffre ses notes de frais « pour que personne ne mette son nez dedans ». Un stagiaire en burn-out a laissé fuiter cette note avant de démissionner. Elle prouverait que les primes du CODIR ont explosé pendant qu'on refusait les congés.

---
 
## Résolution

Dans le fichier on peut trouver : `SG1tZXREamZ2e1B0MXEzeF9RWkRLVl9VM2JvNG52X1AzeF9GM3F1dV9IM19IMGJyM3N9`

Si on le décode en Base64 on trouve : `HmmetDjfv{Pt1q3x_QZDKV_U3bo4nv_P3x_F3quu_H3_H0br3s}`

Ici on peut faire un décodage par vigenère, en faisant un peu de brute-force de la clé on trouve la clé suivante : `FOLACE` et le texte décodé est : `CyberZerk{Pr1m3s_CODIR_P3nd4nt_L3s_R3fus_D3_C0ng3s}`

---
 
## Flag
 
```
CyberZerk{Pr1m3s_CODIR_P3nd4nt_L3s_R3fus_D3_C0ng3s}
```