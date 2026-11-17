# Plan de Charge

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Stéganographie` · **Points** : 241
> **Difficulté** : Difficile  
> **Auteur** : Perseval

---

## Description

Plan de charge de l'équipe (PNG). Message caché dans les bits de poids faible, mais pas dans l'ordre que vous croyez. Graine : 1337. Longueur : 47 octets.

## Fichiers fournis
- plan_de_charge.png

---
 
## Résolution

L'énoncé nous donne trois indices importants :
- `Bits de poids faible (LSB)` : il faut extraire le bit de poids faible des pixels de l'image.
- `Graine : 1337` : l'ordre d'extraction repose sur un générateur pseudo-aléatoire initialisé avec cette graine.
- `Longueur : 47 octets` : le message contient 47 caractères, soit 376 bits à extraire.
La difficulté réside donc dans l'ordre de lecture des pixels. Une extraction classique, pixel par pixel, ne permet pas de retrouver le message.

J'ai utilisé Python avec les bibliothèques Pillow et NumPy pour automatiser l'extraction.

La première étape consiste à ouvrir l'image et à convertir ses pixels en tableau RGB. On initialise ensuite un générateur pseudo-aléatoire avec la graine 1337, puis on utilise permutation() pour obtenir un ordre de lecture différent de celui des pixels d'origine.

```py
from PIL import Image
import numpy as np

# Chargement de l'image
img = Image.open("plan_de_charge.png").convert("RGB")
pixels = np.array(img)

# Génération de l'ordre pseudo-aléatoire
rng = np.random.default_rng(1337)
indices = rng.permutation(pixels.shape[0] * pixels.shape[1])

# Extraction des bits de poids faible du canal bleu
flat = pixels.reshape(-1, 3)
bits = [flat[i, 2] & 1 for i in indices[:47 * 8]]

# Conversion des bits en ASCII
message = bytes(
    sum(bits[i+j] << (7-j) for j in range(8))
    for i in range(0, len(bits), 8)
)

print(message.decode())
```



Quelques explications sur les opérations importantes :
- `np.random.default_rng(1337)` initialise le générateur pseudo-aléatoire avec la graine fournie.
- `permutation()` mélange les indices des pixels pour retrouver leur ordre de lecture.
- `flat[i, 2] & 1` récupère le bit de poids faible du canal bleu de chaque pixel.
- `47 * 8` permet de récupérer les 376 bits correspondant aux 47 octets attendus.
- Enfin, les bits sont regroupés par paquets de 8 et convertis en caractères ASCII.
L'exécution du script permet de retrouver directement le message caché et donc le flag du challenge.

---
 
## Flag
 
```
CyberZerk{lsb_d1sp3rs3_p4r_prng_pas_s3qu3nt13l}
```