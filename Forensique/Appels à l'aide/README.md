# Appels à l'aide

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Forensique` · **Points** : 100
> **Difficulté** : Intro  
> **Auteur** : Perseval

---

## Description

Un analyste SOC de Tricatel a brutalement posé sa démission hier.

Avant de rendre son matériel, l'équipe réseau a remarqué une dernière requête suspecte sortant de son poste vers un serveur non identifié.

Nous avons récupéré une capture de son trafic réseau local.

Analysez cette capture pour retrouver son message d'adieu.

## Fichiers fournis
- appels_a_l_aide.pcap

---
 
## Résolution

C'est un fichier `pcap` donc on peut l'ouvrir avec un outil comme Wireshark. 

Une fois dans Wireshark on peut voir à la 6ème trame ceci : 

```text
0000   00 00 00 00 00 00 00 00 00 00 00 00 08 00 45 00   ..............E.
0010   01 c9 58 d2 40 00 40 06 e2 5a 7f 00 00 01 7f 00   ..X.@.@..Z......
0020   00 01 cb 5a 27 0f 32 3e 67 37 b0 5b 7c 69 80 18   ...Z'.2>g7.[|i..
0030   02 00 ff bd 00 00 01 01 08 0a 9c cd b4 b1 9c cd   ................
0040   b4 af 50 4f 53 54 20 2f 61 64 69 65 75 2e 70 68   ..POST /adieu.ph
0050   70 20 48 54 54 50 2f 31 2e 31 0d 0a 48 6f 73 74   p HTTP/1.1..Host
0060   3a 20 6c 6f 63 61 6c 68 6f 73 74 3a 39 39 39 39   : localhost:9999
0070   0d 0a 41 63 63 65 70 74 3a 20 2a 2f 2a 0d 0a 55   ..Accept: */*..U
0080   73 65 72 2d 41 67 65 6e 74 3a 20 4d 6f 7a 69 6c   ser-Agent: Mozil
0090   6c 61 2f 35 2e 30 20 28 57 69 6e 64 6f 77 73 20   la/5.0 (Windows 
00a0   4e 54 20 31 30 2e 30 3b 20 57 69 6e 36 34 3b 20   NT 10.0; Win64; 
00b0   78 36 34 29 20 42 75 72 6e 6f 75 74 42 72 6f 77   x64) BurnoutBrow
00c0   73 65 72 2f 31 2e 30 0d 0a 43 6f 6e 74 65 6e 74   ser/1.0..Content
00d0   2d 54 79 70 65 3a 20 61 70 70 6c 69 63 61 74 69   -Type: applicati
00e0   6f 6e 2f 78 2d 77 77 77 2d 66 6f 72 6d 2d 75 72   on/x-www-form-ur
00f0   6c 65 6e 63 6f 64 65 64 0d 0a 43 6f 6e 74 65 6e   lencoded..Conten
0100   74 2d 4c 65 6e 67 74 68 3a 20 31 39 38 0d 0a 0d   t-Length: 198...
0110   0a 65 6d 70 6c 6f 79 65 3d 4d 61 72 63 5f 56 26   .employe=Marc_V&
0120   73 74 61 74 75 74 3d 65 70 75 69 73 65 6d 65 6e   statut=epuisemen
0130   74 5f 74 6f 74 61 6c 26 6d 65 73 73 61 67 65 3d   t_total&message=
0140   4a 65 20 71 75 69 74 74 65 20 54 72 69 63 61 74   Je quitte Tricat
0150   65 6c 2e 20 4c 65 20 6d 61 6e 61 67 65 6d 65 6e   el. Le managemen
0160   74 20 6d 65 20 64 c3 a9 74 72 75 69 74 20 6c 61   t me d..truit la
0170   20 73 61 6e 74 c3 a9 20 6d 65 6e 74 61 6c 65 2e    sant.. mentale.
0180   20 4a 65 20 6e 27 61 69 20 70 6c 75 73 20 64 6f    Je n'ai plus do
0190   72 6d 69 20 64 65 70 75 69 73 20 33 20 6a 6f 75   rmi depuis 3 jou
01a0   72 73 2e 20 41 64 69 65 75 2e 20 46 6c 61 67 3a   rs. Adieu. Flag:
01b0   20 43 79 62 65 72 5a 65 72 6b 7b 45 78 66 31 6c    CyberZerk{Exf1l
01c0   74 72 34 74 31 30 6e 5f 48 54 54 50 5f 44 33 73   tr4t10n_HTTP_D3s
01d0   33 73 70 30 31 72 7d                              3sp01r}
```

Si on extrait la valeur entrée dans le formulaire nous avons : 

```text
Value: Je quitte Tricatel. Le management me détruit la santé mentale. Je n'ai plus dormi depuis 3 jours. Adieu. Flag: CyberZerk{Exf1ltr4t10n_HTTP_D3s3sp01r}
```

---
 
## Flag
 
```
CyberZerk{Exf1ltr4t10n_HTTP_D3s3sp01r}
```