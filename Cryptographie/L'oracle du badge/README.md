# L'oracle du badge

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Cryptographie` · **Points** : 191
> **Difficulté** : Moyen  
> **Auteur** : Perseval

---

## Description

Le lecteur de badge chiffre PREFIXE || votre_saisie || SECRET en AES-128-ECB. Le service accepte GET /?data= et renvoie le chiffré. Extrayez le SECRET.

## Fichiers fournis
- oracle_server.py

## Liens fournis
- [https://oracle-badge.cyberzerk.fr](https://oracle-badge.cyberzerk.fr)

---
 
## Résolution

Le challenge met à disposition un oracle de chiffrement AES-128 en mode ECB accessible via une requête HTTP. Celui-ci chiffre systématiquement les données envoyées par l'utilisateur, précédées d'un préfixe aléatoire de 13 octets et suivies du secret à récupérer.

La faiblesse réside dans l'utilisation du mode ECB, qui produit toujours le même bloc chiffré pour un même bloc de données en clair avec une clé identique. Cette propriété permet de réaliser une attaque Byte-at-a-Time ECB Decryption.

J'ai donc développé un script Python qui automatise cette attaque. Il commence par aligner le message sur une frontière de bloc AES en ajoutant 3 octets, puis détermine la longueur du secret. Ensuite, il teste les 256 valeurs possibles pour chaque octet et compare les blocs chiffrés afin de retrouver progressivement le contenu du secret.

Cette méthode permet finalement de récupérer le flag sans connaître ni la clé AES ni le préfixe aléatoire.

Sortie du programme : 

```text
[*] Attaque AES-128-ECB
[*] Oracle : https://oracle-badge.cyberzerk.fr/
[+] Taille du secret : 58
[+] Récupération : CyberZerk{EcB_r3v3l3_1_0ct3t_a_la_f0is_m3m3_av3c_pr3f1x3}

==================================================
[+] SECRET RÉCUPÉRÉ :
CyberZerk{EcB_r3v3l3_1_0ct3t_a_la_f0is_m3m3_av3c_pr3f1x3}
==================================================
```

---
 
## Flag
 
```
CyberZerk{EcB_r3v3l3_1_0ct3t_a_la_f0is_m3m3_av3c_pr3f1x3}
```
