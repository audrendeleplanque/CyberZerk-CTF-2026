# Restructuration

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Secret` · **Points** : 500
> **Difficulté** : Extrême  
> **Auteur** : Perseval

---

## Description

RIEN

---
 
## Résolution

J'ai pu voir sur le discord que des gens avait un challenge secret appelé `Derrière l'armure`. 
J'ai déjà pu voir ce texte quelque part et c'était sur la page du prologue : 

[https://ctf.cyberzerk.fr/prologue](https://ctf.cyberzerk.fr/prologue)

Où ce texte apparait : 

```text
PROLOGUE
Opération CyberZerk : Derrière l'Écran
Il existe un guerrier qui n'a jamais appris à s'arrêter.

Il avance.

Même lorsqu'il est épuisé.
Même lorsqu'il doute.
Même lorsqu'il préférerait faire demi-tour.

Il porte son arme, son armure et tout ce qu'il ne dit jamais.

On lui a appris une chose :

« Continue d'avancer. »

Alors il avance.

Mais quelque chose a changé.

Son armure devient chaque jour plus lourde.

Son énergie diminue.

Et pour la première fois, il comprend que son véritable adversaire n'est peut-être pas devant lui.

Il est temps de regarder ce qui se passe derrière l'armure.
```

En analysant le code source qui est disponible sur `page_prologue.html`, nous pouvons voir qu'il y a des fonction JS qui pointe vers le mot armure avec : 

```js
var mot = document.getElementById('armure');
if (!mot) return;
var clics = 0, ouvert = false;
```

Alors je spam-clic dessus et la page change pour faire apparaitre ceci : 

```text
Fissure Système Détectée

Tu as pris le temps de regarder derrière l'armure.

Voici la clé pour déverrouiller la porte :

CyberZerk{le_masque_tombe}

Copie cette clé et valide-la dans le challenge Derrière l'Armure.
```

---
 
## Flag
 
```
CyberZerk{le_masque_tombe}
```