# Second facteur 

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Sensibilitation` · **Points** : 50
> **Difficulté** : Facile  
> **Auteur** : Perseval

---

## Description

Le portail passe au TOTP (SHA-1, 30 s, 6 chiffres). Secret base32 fourni. Quel code est valide à l'instant Unix T donné ? Flag = CyberZerk{2fa_}.

## Fichiers fournis
- second-facteur-README.txt

---
 
## Résolution

On peut voir dans le fichier texte fourni ce texte : 

```text
Le portail RH passe à la double authentification (TOTP, SHA-1, 30 s, 6 chiffres).
Secret (base32) : JBSWY3DPEHPK3PXP
Quel code est valide à l'instant Unix T = 1762900000 ?
Le flag est CyberZerk{2fa_<code>} (ex. CyberZerk{2fa_123456}).
```

On peut aller sur un site (comme : https://www.base64.sh/totp-generator/) pour générer un code. 

---
 
## Flag
 
```
CyberZerk{2fa_123456} (flag non valable)
```