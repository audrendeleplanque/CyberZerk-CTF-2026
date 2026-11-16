
import random
from pathlib import Path

# 1. Récupération des 624 sorties
tokens = [
    int(x)
    for x in Path("tokens.txt").read_text().splitlines()
    if x.strip()
]

assert len(tokens) == 624

# 2. Inversion du tempering MT19937
MASK = 0xFFFFFFFF

def undo_right(y, shift):
    x = y
    for _ in range(6):
        x = y ^ (x >> shift)
    return x & MASK

def undo_left(y, shift, mask):
    x = y
    for _ in range(6):
        x = y ^ ((x << shift) & mask)
    return x & MASK

def untemper(y):
    y = undo_right(y, 18)
    y = undo_left(y, 15, 0xEFC60000)
    y = undo_left(y, 7, 0x9D2C5680)
    y = undo_right(y, 11)
    return y

# 3. Reconstruction de l'état interne
state = [untemper(x) for x in tokens]

# 4. Restauration du générateur Python
rng = random.Random()
rng.setstate((3, tuple(state + [624]), None))

# 5. Génération des prochains jetons
secret = Path("secret.bin").read_bytes()

keystream = b""

while len(keystream) < len(secret):
    token = rng.getrandbits(32)
    keystream += token.to_bytes(4, "big")

# 6. Déchiffrement XOR
plaintext = bytes(
    a ^ b
    for a, b in zip(secret, keystream)
)

print("[+] État MT19937 reconstruit")
print("[+] Secret déchiffré :")
print(plaintext.decode("utf-8"))

Path("decrypted.txt").write_bytes(plaintext)
print("[+] Résultat sauvegardé dans decrypted.txt")
