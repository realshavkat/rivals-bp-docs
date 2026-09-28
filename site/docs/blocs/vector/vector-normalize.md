---
sidebar_position: 11
title: "Vector.Normalize"
sidebar_label: "Normalize"
description: "Normalize"
---

# Normalize

`Vector.Normalize`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| vector | `vector` | vecteur |  |  |
| flat | `flat` | oui/non | `non` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | vecteur |  |  |

## Détail

- **vector** (`vector`, vecteur). Relie un fil bleu.
- **flat** (`flat`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **résultat** (`result`, vecteur). Relie un fil bleu.
