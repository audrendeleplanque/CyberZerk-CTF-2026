# Clés en Main

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Cryptographie` · **Points** : 175
> **Difficulté** : Difficile  
> **Auteur** : Perseval

---

## Description

On a intercepté la clé publique RSA du DAF et un message chiffré. Le générateur de clés « maison » a été codé à la va-vite une nuit de prod… les deux facteurs premiers se ressemblent étrangement.

## Fichiers fournis
- cle_publique_et_message.txt

---
 
## Résolution

En utilisant ce script python : 

```py

#!/usr/bin/env python3
"""
CyberZerk CTF - RSA Fermat Attack
Objectif : Factoriser n lorsque p et q sont trop proches,
puis reconstruire la clé privée et déchiffrer le message.
"""

from math import isqrt


# ============================================================
# 1. Paramètres RSA récupérés dans le fichier d'interception
# ============================================================

n = 80212772058200318331300079496309046404407863541893990823458017701424496169728020886315708954946247456549467636228289508051504043657362562710963459898059618322307640646997491893098662379623269687517308992271177299514157669726203684540391560112332919658354699766234227531947934780484232345671991558901521674857

e = 65537

c = 37349549515090945417450122795335580990902750723340185050711772061916623126113099880177602219381069951334085720404628406456724149937589057117852268813232105608362675774617868234377809159128266125490782550531069542420297187328167250214392422812890728320489416372899423467921565710232771608025776495955836994422


# ============================================================
# 2. Factorisation de n avec la méthode de Fermat
# ============================================================

def fermat_factorization(n):
    """
    Recherche deux facteurs p et q tels que :
        n = p * q

    La méthode de Fermat exploite la proximité
    des deux facteurs premiers.
    """

    a = isqrt(n)

    if a * a < n:
        a += 1

    while True:
        b_squared = a * a - n
        b = isqrt(b_squared)

        if b * b == b_squared:
            p = a - b
            q = a + b

            if p * q == n:
                return p, q

        a += 1


print("[+] Factorisation de n...")

p, q = fermat_factorization(n)

print(f"[+] p = {p}")
print(f"[+] q = {q}")
print(f"[+] Vérification : p * q == n : {p * q == n}")


# ============================================================
# 3. Reconstruction de la clé privée RSA
# ============================================================

print("\n[+] Reconstruction de la clé privée...")

# Calcul de la fonction indicatrice d'Euler
phi = (p - 1) * (q - 1)

# Calcul de l'exposant privé d
d = pow(e, -1, phi)

print(f"[+] Exposant privé d = {d}")


# ============================================================
# 4. Déchiffrement du message
# ============================================================

print("\n[+] Déchiffrement du message...")

# Formule RSA : m = c^d mod n
m = pow(c, d, n)

# Conversion de l'entier en bytes
message = m.to_bytes(
    (m.bit_length() + 7) // 8,
    byteorder="big"
)

# Affichage du résultat
print("\n" + "=" * 60)
print("[+] MESSAGE DECHIFFRE")
print("=" * 60)

try:
    print(message.decode("utf-8"))
except UnicodeDecodeError:
    print(message.hex())

print("=" * 60)
```

Nous avons cette sortie :

```text
[+] Factorisation de n...
[+] Vérification : p * q == n : True

[+] Reconstruction de la clé privée...

[+] Déchiffrement du message...

============================================================
[+] MESSAGE DECHIFFRE
============================================================
CyberZerk{F3rm4t_C4ss3_L3s_Pr3m13rs_Tr0p_Pr0ch3s}
============================================================
```

---
 
## Flag
 
```
CyberZerk{F3rm4t_C4ss3_L3s_Pr3m13rs_Tr0p_Pr0ch3s}
```