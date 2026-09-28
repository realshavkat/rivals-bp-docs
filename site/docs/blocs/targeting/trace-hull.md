---
sidebar_position: 5
title: "Trace.Hull"
sidebar_label: "Hull"
description: "Trace en boîte (longueur max"
---

# Trace en boîte (longueur max

`Trace.Hull`

Trace en boîte (longueur max

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

Chaque passage consomme **6** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| start | `start` | vecteur |  |  |
| stop | `stop` | vecteur |  |  |
| size | `size` | nombre | `16` | de 1 à 128 |

## Sorties

Aucune.

## Détail

- **start** (`start`, vecteur). Relie un fil bleu.
- **stop** (`stop`, vecteur). Relie un fil bleu.
- **size** (`size`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `16`. Borné de 1 à 128.
