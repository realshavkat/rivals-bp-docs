---
sidebar_position: 7
title: "Math.Lerp"
sidebar_label: "Lerp"
description: "Lerp"
---

# Lerp

`Math.Lerp`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| a | `a` | nombre | `0` | de -1000000 à 1000000 |
| b | `b` | nombre | `1` | de -1000000 à 1000000 |
| t | `t` | nombre | `0.5` | de 0 à 1 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | nombre |  |  |

## Détail

- **a** (`a`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **b** (`b`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de -1000000 à 1000000.
- **t** (`t`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.5`. Borné de 0 à 1.
- **résultat** (`result`, nombre). Relie un fil bleu.
