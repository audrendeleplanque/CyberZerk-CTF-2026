# Double fond

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Stéganographie` · **Points** : 175
> **Difficulté** : Difficile  
> **Auteur** : Perseval

---

## Description

Une affiche de « gestion de crise » circule. Elle cache deux choses : une clé, rangée proprement dans l'image, et un message, collé juste après. L'un sert à lire l'autre.

## Fichiers fournis
- affiche_crise.png

---
 
## Résolution

### Étape 1 : analyse de la structure du PNG
 
Un PNG est une suite de chunks (`IHDR`, `IDAT`, `IEND`, etc.). En les parcourant, on trouve :
 
- un chunk `tEXt` placé entre `IHDR` et `IDAT`, de mot-clé `cle`, qui contient `Y3IxczMtdGMyNg==` ;
- 35 octets supplémentaires après le chunk `IEND`, que les lecteurs d'images ignorent.
```bash
pngcheck -v affiche_crise.png     # liste les chunks et signale les données après IEND
exiftool affiche_crise.png        # affiche le champ « cle »
tail -c 35 affiche_crise.png | xxd
```
 
### Étape 2 : récupération de la clé
 
La valeur du chunk `tEXt` est du base64 :
 
```
Y3IxczMtdGMyNg==  →  cr1s3-tc26
```
 
### Étape 3 : déchiffrement du message
 
Les 35 octets après `IEND` ne sont pas lisibles directement. Comme l'énoncé dit que la clé « sert à lire » le message, on applique un XOR avec la clé `cr1s3-tc26` répétée en boucle (XOR à clé répétée) :
 
```python
import base64
 
d = open("affiche_crise.png", "rb").read()
key = base64.b64decode("Y3IxczMtdGMyNg==")
payload = d[-35:]
print(bytes(b ^ key[i % len(key)] for i, b in enumerate(payload)))
```

Sortie du programme : `CyberZerk{St3g0_Pu1s_X0R_B13n_J0u3}`

---
 
## Flag
 
```
CyberZerk{St3g0_Pu1s_X0R_B13n_J0u3}
```