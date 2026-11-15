# La Porte de Service 

> **CTF** : CyberZerk 2026  
> **Catégorie** : `Divers` · **Points** : 125
> **Difficulté** : Difficile  
> **Auteur** : Perseval

---

## Description

Challenge non listé. Une capture de la réponse du service de maintenance est fournie. Le corps ne dit rien... mais les serveurs parlent aussi par leurs en-têtes.

## Fichiers fournis
- README_2.txt
- reponse_http.txt

---
 
## Résolution

Dans le fichier `README_2.txt` nous avons ce texte : 

```text
Capture d'une réponse du service de maintenance Tricatel (reponse_http.txt).
Le service ne montre rien d'intéressant dans son corps... mais les serveurs parlent
aussi par leurs en-têtes. Une porte de service a été laissée ouverte.
```

Ca nous donne un indice sur ce qu'il faut regarder, il faut regarder les en-têtes. 

Et dans le fichier `reponse_http.txt` nous avons : 

```text
GET / HTTP/1.1
Host: intranet.tricatel.local

HTTP/1.1 200 OK
Date: Sat, 14 Nov 2026 09:12:44 GMT
Server: Apache/2.4.58 (Debian)
X-Powered-By: PHP/8.3.6
Cache-Control: no-store
Content-Type: text/plain; charset=utf-8
X-Frame-Options: SAMEORIGIN
X-Service-Door: Q3liZXJaZXJre3AwcnQzX2QzX3MzcnYxYzNfY2FjaDMzX2RhbnNfdW5fM250M3QzfQ==
Set-Cookie: session=deleted; expires=Thu, 01 Jan 1970 00:00:00 GMT
Content-Length: 41

Intranet Tricatel — maintenance en cours.
```

Une chose saute aux yeux qui est la valeur de `X-Service-Door` qui est `Q3liZXJaZXJre3AwcnQzX2QzX3MzcnYxYzNfY2FjaDMzX2RhbnNfdW5fM250M3QzfQ==`. 

Une fois décodée en Base64 cela donne : `CyberZerk{p0rt3_d3_s3rv1c3_cach33_dans_un_3nt3t3}`

---
 
## Flag
 
```
CyberZerk{p0rt3_d3_s3rv1c3_cach33_dans_un_3nt3t3}
```