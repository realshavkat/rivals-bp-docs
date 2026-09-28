---
sidebar_position: 10
title: "Status.Has"
sidebar_label: "Has"
description: "Has"
---

# Has

`Status.Has`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |
| status | `status` | texte | `stun` | choix: `slow`, `root`, `stun`, `dribble_immune` |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | oui/non |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **status** (`status`, texte). Sans fil bleu, le défaut est utilisé. Défaut: `stun`. Valeurs prévues: `slow`, `root`, `stun`, `dribble_immune`.
- **résultat** (`result`, oui/non). Relie un fil bleu.
