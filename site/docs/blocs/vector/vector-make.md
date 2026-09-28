---
sidebar_position: 10
title: "Vector.Make"
sidebar_label: "Make"
description: "Make"
---

# Make

`Vector.Make`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| x | `x` | nombre | `0` | de -1000000 à 1000000 |
| y | `y` | nombre | `0` | de -1000000 à 1000000 |
| z | `z` | nombre | `0` | de -1000000 à 1000000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| vector | `vector` | vecteur |  |  |

## Détail

- **x** (`x`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **y** (`y`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **z** (`z`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **vector** (`vector`, vecteur). Relie un fil bleu.
