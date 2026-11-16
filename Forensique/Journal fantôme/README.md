# Journal fantôme

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Forensique` · **Points** : 172
> **Difficulté** : Moyen  
> **Auteur** : Perseval

---

## Description

Extrait de la base de la pointeuse. Un pointage nocturne a été 'effacé' : les requêtes ne le montrent plus. Retrouvez-le.

## Fichiers fournis
- pointeuse.sqlite

---
 
## Résolution

Il suffit de faire la commande `strings` sur le fichier `.sqlite` et nous avons ceci : 

```text
SQLite format 3
;tablepointagespointages
CREATE TABLE pointages(id INTEGER PRIMARY KEY, agent TEXT, badge TEXT, horodatage TEXT)
-DAFB-10032026-11-03 08:30
i-ADMIN_SYSCyberZerk{sql1t3_d3l3t3_n3_v1d3_pas_l3s_p4g3s}2026-11-03 02:03
-DRHB-10012026-11-03 07:45!
-DidierB-10122026-11-03 09:14!
-Marc_VB-10072026-11-03 08:59
```

---
 
## Flag
 
```
CyberZerk{sql1t3_d3l3t3_n3_v1d3_pas_l3s_p4g3s}
```