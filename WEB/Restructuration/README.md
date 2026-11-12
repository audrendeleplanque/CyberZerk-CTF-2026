# Restructuration

> **CTF** : CyberZerk 2026  
> **Catégorie** : `WEB` · **Points** : 175
> **Difficulté** : Difficile  
> **Auteur** : Perseval

---

## Description

Le « générateur d'aperçus de rapports » de Tricatel va chercher pour vous le contenu d'une URL. Un coffre RH interne (interne.php) n'est censé être joignable que depuis le réseau de l'application. Faites parler le serveur à votre place.

## Liens fournis
- [https://restructuration.cyberzerk.fr](https://restructuration.cyberzerk.fr)

---
 
## Résolution

L'application « générateur d'aperçus de rapports » de Tricatel permet de soumettre une URL dont le serveur va récupérer le contenu. Un endpoint interne, `interne.php`, n'est censé répondre qu'aux requêtes provenant du réseau interne de l'application.

### Vulnérabilité

Deux couches de protection distinctes ont été identifiées :

1. **Filtre côté formulaire** : bloque les URL contenant littéralement les chaînes `127.0.0.1` ou `localhost` (vérification textuelle, pas de résolution réelle de l'adresse).
2. **Contrôle d'accès côté `interne.php`** : vérifie l'IP source de la requête entrante, et rejette tout ce qui n'arrive pas depuis `127.0.0.1`.

Le point clé : `interne.php` est servi sur un **port non standard** (`8080`), séparé du reverse-proxy public (qui, lui, écoute sur 80/443 et réécrit toute IP source en `172.23.0.3`). Une requête directe vers le port 8080 en loopback atteint donc le service sans passer par le proxy, avec la bonne IP source.

Il restait à contourner le filtre textuel de la couche 1 sans perdre la résolution réelle en loopback côté client HTTP. Solution : utiliser une **représentation alternative de l'adresse IP** que le filtre ne reconnaît pas comme telle, mais que le client HTTP résout correctement.

### Exploitation

Payload final soumis dans le formulaire :

```
http://0x7f000001:8080/interne.php
```

- `0x7f000001` est la notation hexadécimale de `127.0.0.1`.
- Le filtre, basé sur un pattern-matching textuel (`127.0.0.1` / `localhost`), ne reconnaît pas cette forme et laisse passer la requête.
- Le client HTTP du serveur (curl ou équivalent), lui, interprète correctement `0x7f000001` comme `127.0.0.1` et s'y connecte.
- Le port `8080` cible directement le service interne, en contournant le reverse-proxy.

Résultat : `interne.php` reçoit la requête depuis `127.0.0.1`, la valide, et retourne le contenu du coffre RH.

```text
COFFRE RH INTERNE
Primes CODIR, dossiers medicaux... et le drapeau :
CyberZerk{SSRF_V3rs_L3_C0ffr3_Int3rn3}
```

---
 
## Flag
 
```
CyberZerk{SSRF_V3rs_L3_C0ffr3_Int3rn3}
```