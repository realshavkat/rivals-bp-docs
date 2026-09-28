---
sidebar_position: 6
title: "Balance.Scale"
sidebar_label: "Scale"
description: "Multiplie une valeur par un facteur d'équilibrage."
---

# Multiplie une valeur par un facteur d'équilibrage

`Balance.Scale`

Multiplie une valeur par un facteur d'équilibrage.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| valeur | `value` | nombre | `1` | de -1000000 à 1000000 |
| mult | `mult` | nombre | `1` | de 0 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | nombre |  |  |

## Détail

- **valeur** (`value`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de -1000000 à 1000000.
- **mult** (`mult`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0 à 10.
- **résultat** (`result`, nombre). Relie un fil bleu.
