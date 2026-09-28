---
sidebar_position: 1
title: "Anim.Duration"
sidebar_label: "Duration"
description: "Duration"
---

# Duration

`Anim.Duration`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |
| animation | `sequence` | texte |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| durée | `duration` | nombre |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **animation** (`sequence`, texte). Relie un fil bleu.
- **durée** (`duration`, nombre). Relie un fil bleu.
