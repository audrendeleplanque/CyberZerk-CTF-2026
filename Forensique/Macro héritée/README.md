# Macro héritée

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Forensique` · **Points** : 176
> **Difficulté** : Moyen  
> **Auteur** : Perseval

---

## Description

Macro extraite du classeur suspect du DRH. Que révèle-t-elle à l'ouverture ?

## Fichiers fournis
- macro.vba

---
 
## Résolution

Dans le fichier `macro.vba` nous avons ceci : 

```text
Chr(102) & Chr(84) & Chr(78) & Chr(122) & Chr(99) & Chr(106) & Chr(78) & Chr(50) & Chr(77) & Chr(51) & Chr(74) & Chr(102) & Chr(78) & Chr(68) & Chr(90) & Chr(105) & Chr(88) & Chr(51) & Chr(74) & Chr(111) & Chr(89) & Chr(49) & Chr(56) & Chr(122) & Chr(98) & Chr(109) & Chr(107) & Chr(48) & Chr(97) & Chr(71) & Chr(78) & Chr(102) & Chr(98) & Chr(106) & Chr(65) & Chr(120) & Chr(100) & Chr(68) & Chr(82) & Chr(106) & Chr(99) & Chr(51) & Chr(86) & Chr(109) & Chr(89) & Chr(106) & Chr(66) & Chr(122) & Chr(77) & Chr(50) & Chr(82) & Chr(102) & Chr(89) & Chr(87) & Chr(74) & Chr(50) & Chr(101) & Chr(50) & Chr(116) & Chr(121) & Chr(90) & Chr(86) & Chr(112) & Chr(121) & Chr(90) & Chr(87) & Chr(74) & Chr(53) & Chr(81) & Chr(119) & Chr(61) & Chr(61)
```

Si nous enlevons toutes les fonctions `Chr()` nous avons ceci : 

```text
102 84 78 122 99 106 78 50 77 51 74 102 78 68 90 105 88 51 74 111 89 49 56 122 98 109 107 48 97 71 78 102 98 106 65 120 100 68 82 106 99 51 86 109 89 106 66 122 77 50 82 102 89 87 74 50 101 50 116 121 90 86 112 121 90 87 74 53 81 119 61 61
```

Chaque chiffre est un caractère en ASCII, une fois décodé nous avons : 

```text
fTNzcjN2M3JfNDZiX3JoY18zbmk0aGNfbjAxdDRjc3VmYjBzM2RfYWJ2e2tyZVpyZWJ5Qw==
```

Cela ressemble à du `Base64` et une fois décodé nous avons : 

```text
}3sr3v3r_46b_rhc_3ni4hc_n01t4csufb0s3d_abv{kreZrebyC
```

Pour finir nous devons faire un fonction `reverse` qui inverse chaque lettres ce qui donne : 

```text
CyberZerk{vba_d3s0bfusc4t10n_ch4in3_chr_b64_r3v3rs3}
```

---
 
## Flag
 
```
CyberZerk{vba_d3s0bfusc4t10n_ch4in3_chr_b64_r3v3rs3}
```