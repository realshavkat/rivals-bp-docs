---
sidebar_position: 5
title: "Math.Div"
sidebar_label: "Div"
description: "Divise a par b. Si b vaut 0, le résultat est 0."
---

# Divise a par b. Si b vaut 0, le résultat est 0

`Math.Div`

Divise a par b. Si b vaut 0, le résultat est 0.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| a | `a` | nombre | `0` | de -1000000 à 1000000 |
| b | `b` | nombre | `0` | de -1000000 à 1000000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | nombre |  |  |

## Détail

- **a** (`a`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **b** (`b`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **résultat** (`result`, nombre). Relie un fil bleu.
