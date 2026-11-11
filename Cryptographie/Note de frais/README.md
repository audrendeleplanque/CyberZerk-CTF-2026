# La minute bien être

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Cryptographie` · **Points** : 75
> **Difficulté** : Facile  
> **Auteur** : Perseval

---

## Description

Extrait du journal de bord de l'analyste - Jour 43.

"Je n'arrive plus à avancer. À chaque fois que j'essaie de rédiger ce rapport, cette voix dans ma tête revient. Elle brouille mes pensées, elle chiffre mes certitudes. Elle me répète sans cesse la même chose, en boucle, comme une fatalité : je suis nul."

J'ai essayé d'écrire une note pour me rassurer, pour me rappeler qui je suis. Mais la voix a pris le dessus. Mon propre message d'espoir a été chiffré par sa rengaine, utilisant une méthode de substitution séculaire attribuée à un diplomate français du 16ème siècle.

Voici la note que j'ai retrouvée ce matin sur mon bureau : LctyzRrlv{Cy_Sm_Bs_Cflli_Awq}

## Fichiers fournis
- note_chiffree.txt

---
 
## Résolution

Dans l'énoncé on peut trouver : `LctyzRrlv{Cy_Sm_Bs_Cflli_Awq}`

Ici on peut faire un décodage par vigenère, en faisant un peu de brute-force de la clé on trouve la clé suivante : `jesuisnul` et le texte décodé est : `CyberZerk{Tu_As_Ta_Place_Ici}`

---
 
## Flag
 
```
CyberZerk{Tu_As_Ta_Place_Ici}
```