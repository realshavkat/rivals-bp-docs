---
sidebar_position: 2
title: "Entity.GetVelocity"
sidebar_label: "GetVelocity"
description: "GetVelocity"
---

# GetVelocity

`Entity.GetVelocity`

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
| velocity | `velocity` | vecteur |  |  |
| vitesse | `speed` | nombre |  |  |

## Détail

- **cible** (`entity`, entité). Relie un fil bleu.
- **velocity** (`velocity`, vecteur). Relie un fil bleu.
- **vitesse** (`speed`, nombre). Relie un fil bleu.
