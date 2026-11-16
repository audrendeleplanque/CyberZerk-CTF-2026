# Frappes captées

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Forensique` · **Points** : 176
> **Difficulté** : Moyen  
> **Auteur** : Perseval

---

## Description

Capture USB d'un clavier branché sur un poste. Reconstituez ce qui a été tapé.

## Fichiers fournis
- frappes.pcap

---
 
## Résolution

Comment je l'ai retrouvé
1. Identification du format PCAP : capture USB Linux.
2. Extraction des rapports HID de 8 octets.
3. Identification des touches à partir de leurs codes HID.
4. Prise en compte du modificateur `Shift` (0x02).
5. Reconstruction du texte en ignorant les rapports correspondant au relâchement des touches.

---
 
## Flag
 
```
CyberZerk{usb_h1d_k3yb0ard_r3p0rt_8_0ct3ts}
```