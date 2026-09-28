---
sidebar_position: 6
title: "Player.IsGrounded"
sidebar_label: "IsGrounded"
description: "IsGrounded"
---

# IsGrounded

`Player.IsGrounded`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| cible | `entity` | entité |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | oui/non |  |  |

## Détail

- **cible** (`entity`, entité). Relie un fil bleu.
- **résultat** (`result`, oui/non). Relie un fil bleu.
