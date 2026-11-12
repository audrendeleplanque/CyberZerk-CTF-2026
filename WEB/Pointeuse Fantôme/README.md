# Pointeuse Fantôme

> **CTF** : CyberZerk 2026  
> **Catégorie** : `WEB` · **Points** : 50
> **Difficulté** : Intro  
> **Auteur** : Perseval

---

## Description

Le nouveau logiciel de pointage de Tricatel « oublie » discrètement les heures supplémentaires. Vous n'avez accès qu'à votre fiche. Pourtant, quelqu'un a bien le droit de voir les heures réelles de toute l'équipe…

## Liens fournis
- [https://pointeuse.cyberzerk.fr](https://pointeuse.cyberzerk.fr)

---
 
## Résolution

On peut voir que dans les cookies nous avon un cookie `profil`

Après décodage, on obtient le contenu suivant :

```json
{
  "employe": "Vous (#8472)",
  "role": "employe"
}
```

Le cookie contient donc directement le rôle de l'utilisateur. Aucune signature ou protection ne semble empêcher sa modification.

Il suffit alors de remplacer la valeur du champ `role` par `manager`, puis de réencoder le JSON en Base64 :

```json
{
  "employe": "Vous (#8472)",
  "role": "manager"
}
```

Une fois réencoder en Base64 nous avons : `eyJlbXBsb3llIjoiVm91cyAoIzg0NzIpIiwicm9sZSI6Im1hbmFnZXIifQ==`

Après avoir remplacé le cookie `profil` dans le navigateur et actualisé la page, l'application reconnaît l'utilisateur comme manager et donne accès au registre réel des heures de toute l'équipe.

---
 
## Flag
 
```
CyberZerk{P0int3us3_Qu1_0ubl13_L3s_H3ur3s_Sup}
```