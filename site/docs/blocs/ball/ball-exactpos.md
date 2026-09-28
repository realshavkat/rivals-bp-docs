---
sidebar_position: 1
title: "Ball.ExactPos"
sidebar_label: "ExactPos"
description: "Position exacte du ballon au pied du joueur (BL:GetExactBallPos)."
---

# Position exacte du ballon au pied du joueur (BL:GetExactBallPos)

`Ball.ExactPos`

Position exacte du ballon au pied du joueur (BL:GetExactBallPos).

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Ball.ExactPos(player = caster)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| pos | `pos` | vecteur |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **pos** (`pos`, vecteur). Relie un fil bleu.
