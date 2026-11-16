
import requests

# =====================================================
# CONFIGURATION
# =====================================================

TARGET = "https://oracle-badge.cyberzerk.fr/"

BLOCK_SIZE = 16

# Le préfixe du challenge fait 13 octets.
PREFIX_LENGTH = 13

# =====================================================
# ORACLE AES-ECB
# =====================================================

def oracle(data: bytes) -> bytes:
    response = requests.get(
        TARGET,
        params={"data": data.hex()},
        timeout=10
    )

    response.raise_for_status()

    return bytes.fromhex(response.text.strip())


# =====================================================
# DÉTECTION DE LA LONGUEUR DU SECRET
# =====================================================

def find_secret_length():

    # Trois octets permettent de compléter le préfixe
    alignment = b"A" * (BLOCK_SIZE - PREFIX_LENGTH)

    initial_length = len(oracle(alignment))

    for i in range(1, BLOCK_SIZE + 1):

        current_length = len(
            oracle(alignment + b"A" * i)
        )

        if current_length > initial_length:

            # Nombre d'octets avant le padding
            secret_length = (
                initial_length
                - len(alignment)
                - PREFIX_LENGTH
                - (i - 1)
            )

            return secret_length

    raise RuntimeError("Impossible de détecter la longueur du secret")


# =====================================================
# RÉCUPÉRATION DU SECRET
# =====================================================

def recover_secret():

    alignment = b"A" * (BLOCK_SIZE - PREFIX_LENGTH)

    secret_length = find_secret_length()

    print(f"[+] Taille du secret : {secret_length}")

    recovered = b""

    for position in range(secret_length):

        # Nombre d'octets nécessaires pour aligner
        # le prochain caractère sur la fin d'un bloc
        padding_length = BLOCK_SIZE - 1 - (position % BLOCK_SIZE)

        padding = b"A" * padding_length

        # Bloc contenant le caractère recherché
        block_index = 1 + position // BLOCK_SIZE

        reference = oracle(alignment + padding)

        target_block = reference[
            block_index * BLOCK_SIZE:
            (block_index + 1) * BLOCK_SIZE
        ]

        found = False

        # Test des 256 valeurs possibles
        for candidate in range(256):

            attempt = (
                alignment
                + padding
                + recovered
                + bytes([candidate])
            )

            encrypted = oracle(attempt)

            candidate_block = encrypted[
                block_index * BLOCK_SIZE:
                (block_index + 1) * BLOCK_SIZE
            ]

            if candidate_block == target_block:

                recovered += bytes([candidate])

                print(
                    f"\r[+] Récupération : "
                    f"{recovered.decode(errors='replace')}",
                    end="",
                    flush=True
                )

                found = True
                break

        if not found:

            print(
                f"\n[-] Impossible de récupérer "
                f"le caractère {position}"
            )

            return recovered

    print("\n\n" + "=" * 50)
    print("[+] SECRET RÉCUPÉRÉ :")
    print(recovered.decode(errors="replace"))
    print("=" * 50)

    return recovered


# =====================================================
# PROGRAMME PRINCIPAL
# =====================================================

if __name__ == "__main__":

    print("[*] Attaque AES-128-ECB")
    print("[*] Oracle :", TARGET)

    try:
        recover_secret()

    except requests.RequestException as error:
        print("\n[-] Erreur HTTP :", error)

    except Exception as error:
        print("\n[-] Erreur :", error)
