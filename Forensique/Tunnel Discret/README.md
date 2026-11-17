# Tunnel Discret

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Forensique` · **Points** : 175
> **Difficulté** : Difficile  
> **Auteur** : Perseval

---

## Description

Capture réseau d'un poste. Un processus parle beaucoup au DNS. Que fait-il sortir ?

## Fichiers fournis
- capture.pcap

---
 
## Résolution

La capture contient 14 paquets, tous des requêtes DNS envoyées par `10.10.0.57` vers le résolveur `10.10.0.1`.

- Quatre requêtes sont banales : `intranet`, `mail`, `wiki` et `proxy.tricatel-interne.fr`.
- Dix requêtes ont une forme suspecte : `NN.<12 caractères hexa>.exfil-4167c682.tricatel-interne.fr`.

Le premier label (`00` à `09`) est un numéro de séquence, utile parce que le DNS ne garantit pas l'ordre d'arrivée. Le second est un fragment de données encodé en hexadécimal. Le domaine `exfil-…` est celui d'un serveur DNS contrôlé par l'attaquant, qui reçoit les fragments dans les requêtes.

On extrait le deuxième label de chaque requête, dans l'ordre de la séquence, puis on décode l'hexa en ASCII :

```python
chunks = ["43796265725a", "65726b7b646e", "735f33786631", "6c7472347431",
          "306e5f723334", "7373336d626c", "335f6c33735f", "733075735f64",
          "306d34316e33", "737d"]
print(bytes.fromhex("".join(chunks)).decode())
```

---
 
## Flag
 
```
CyberZerk{dns_3xf1ltr4t10n_r34ss3mbl3_l3s_s0us_d0m41n3s}
```