---
sidebar_position: 1
title: "Target.FindBallInCone"
sidebar_label: "FindBallInCone"
description: "Ballon dans le cône de visée."
---

# Ballon dans le cône de visée

`Target.FindBallInCone`

Ballon dans le cône de visée.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Dans la vue Code, le verbe est [`find_ball`](/langage/verbes#find_ball) : `find_ball(range, angle)`.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

Chaque passage consomme **6** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |
| portée | `range` | nombre | `150` | de 16 à 3000 |
| angle | `angle` | nombre | `60` | de 1 à 180 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| ball | `ball` | entité |  |  |
| found | `found` | oui/non |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **portée** (`range`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `150`. Borné de 16 à 3000.
- **angle** (`angle`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `60`. Borné de 1 à 180.
- **ball** (`ball`, entité). Relie un fil bleu.
- **found** (`found`, oui/non). Relie un fil bleu.
