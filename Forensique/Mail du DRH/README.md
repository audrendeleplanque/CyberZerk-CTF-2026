# Mail du DRH

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Forensique` · **Points** : 75
> **Difficulté** : Facile  
> **Auteur** : Perseval

---

## Description

On vous transmet un mail interne du DRH, « authentique » selon lui. Les salariés jurent ne l'avoir jamais envoyé. Prouvez d'où il vient vraiment et ce qu'il cache.

## Fichiers fournis
- note_du_drh.eml

---
 
## Résolution

Un fichier `.eml` est un fichier mail donc on peut l'ouvrir avec des outils en ligne ou directement dans notre boite mail. 

Dans ce mail on peut lire un mail de la DRH et une pièce jointe (`note_interne_rh.txt`). Dans cette piece jointe on peut lire : 

```text
NOTE INTERNE - CONFIDENTIEL RH
Objet : surveillance des arrets maladie

Consigne de la Direction : contester systematiquement les arrets
de plus de 3 jours et bloquer les acces informatiques du salarie.
Ne pas laisser de trace ecrite cote salarie.

Preuve de l'ordre : CyberZerk{M4il_Sp00f3_P0ur_Surv31ll3r_L3s_Arr3ts}
```

---
 
## Flag
 
```
CyberZerk{M4il_Sp00f3_P0ur_Surv31ll3r_L3s_Arr3ts}
```