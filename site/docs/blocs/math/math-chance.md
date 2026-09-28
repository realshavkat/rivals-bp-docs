---
sidebar_position: 3
title: "Math.Chance"
sidebar_label: "Chance"
description: "Vrai avec une probabilité de 'percent' %."
---

# Vrai avec une probabilité de 'percent' %

`Math.Chance`

Vrai avec une probabilité de 'percent' %.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Dans la vue Code, le verbe est [`chance`](/langage/verbes#chance) : `chance(percent)`.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| percent | `percent` | nombre | `50` | de 0 à 100 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | oui/non |  |  |

## Détail

- **percent** (`percent`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `50`. Borné de 0 à 100.
- **résultat** (`result`, oui/non). Relie un fil bleu.
