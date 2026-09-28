---
sidebar_position: 1
title: "Entity.GetPos"
sidebar_label: "GetPos"
description: "GetPos"
---

# GetPos

`Entity.GetPos`

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
| pos | `pos` | vecteur |  |  |
| center | `center` | vecteur |  |  |

## Détail

- **cible** (`entity`, entité). Relie un fil bleu.
- **pos** (`pos`, vecteur). Relie un fil bleu.
- **center** (`center`, vecteur). Relie un fil bleu.
