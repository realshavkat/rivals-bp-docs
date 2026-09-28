---
sidebar_position: 2
title: "Angle.Make"
sidebar_label: "Make"
description: "Make"
---

# Make

`Angle.Make`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| pitch | `pitch` | nombre | `0` | de -1000000 à 1000000 |
| yaw | `yaw` | nombre | `0` | de -1000000 à 1000000 |
| roll | `roll` | nombre | `0` | de -1000000 à 1000000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| angle | `angle` | angle |  |  |

## Détail

- **pitch** (`pitch`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **yaw** (`yaw`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **roll** (`roll`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **angle** (`angle`, angle). Relie un fil bleu.
