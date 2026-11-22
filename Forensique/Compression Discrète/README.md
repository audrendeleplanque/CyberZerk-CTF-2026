# Compression discrète

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Forensique` · **Points** : 228
> **Difficulté** : Difficile  
> **Auteur** : Perseval

---

## Description

Photo de l'open space en JPEG. Le message ne survit pas dans les pixels… mais dans la compression ?

## Fichiers fournis
- compression-discrete-photo.jpg

---
 
## Résolution

Le JPEG est un JPEG baseline classique de 480×360, avec un sous-échantillonnage 4:2:0 (blocs 2×2 pour la luminance). Il n’y a ni commentaire, ni EXIF, ni données ajoutées après le marqueur de fin FFD9. Le message n’est donc pas dans les métadonnées, mais bien dans les coefficients DCT quantifiés, comme l’énoncé le laisse entendre avec « dans la compression ».
La technique est JSteg : on cache un bit dans le bit de poids faible (LSB) de chaque coefficient AC, en laissant de côté les coefficients valant 0, 1 ou -1.
J’ai lu les coefficients avec jpeglib (Pillow ne les expose pas), en prenant le canal de luminance Y, les 63 coefficients AC de chaque bloc en ordre zigzag, et les bits dans chaque octet du poids faible vers le poids fort. L’ordre des blocs est celui du flux JPEG (MCU entrelacés).

```py
import jpeglib, numpy as np
im = jpeglib.read_dct("compression-discrete-photo.jpg")
zz = [0,1,8,16,9,2,3,10,17,24,32,25,18,11,4,5,12,19,26,33,40,48,41,34,27,20,13,6,7,14,21,28,
      35,42,49,56,57,50,43,36,29,22,15,23,30,37,44,51,58,59,52,45,38,31,39,46,53,60,61,54,47,55,62,63]
Y = im.Y; bh, bw = Y.shape[:2]
vals = []
for mr in range(0, bh, 2):
    for mc in range(0, bw, 2):
        for dr in (0, 1):
            for dc in (0, 1):
                if mr+dr < bh and mc+dc < bw:
                    blk = Y[mr+dr, mc+dc].reshape(64)
                    vals += [int(blk[zz[k]]) for k in range(1, 64) if int(blk[zz[k]]) not in (0, 1, -1)]
bits = np.array([v & 1 for v in vals], dtype=np.uint8)
n = len(bits)//8
data = np.packbits(bits[:n*8].reshape(n, 8)[:, ::-1], axis=1).reshape(-1).tobytes()
print(data[:70])   # b'jsteg.\x00\x00\x00CyberZerk{jst3g_lsb_d3s_c03ff1c13nts_dct_jp3g}...'
```

---
 
## Flag
 
```
CyberZerk{jst3g_lsb_d3s_c03ff1c13nts_dct_jp3g}
```