---
sidebar_position: 2
title: "Ball.Get"
sidebar_label: "Get"
description: "Ballon du joueur (ball, hasBall)."
---

# Ballon du joueur (ball, hasBall)

`Ball.Get`

Ballon du joueur (ball, hasBall).

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Dans la vue Code, le verbe est [`ball`](/langage/verbes#ball).

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| ball | `ball` | entité |  |  |
| hasBall | `hasBall` | oui/non |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **ball** (`ball`, entité). Relie un fil bleu.
- **hasBall** (`hasBall`, oui/non). Relie un fil bleu.
