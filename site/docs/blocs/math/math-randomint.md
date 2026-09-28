---
sidebar_position: 11
title: "Math.RandomInt"
sidebar_label: "RandomInt"
description: "RandomInt"
---

# RandomInt

`Math.RandomInt`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Math.RandomInt(min = 1, max = 6)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| min | `min` | entier | `1` | de … à 1000000 |
| max | `max` | entier | `6` | de … à 1000000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | entier |  |  |

## Détail

- **min** (`min`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de … à 1000000.
- **max** (`max`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `6`. Borné de … à 1000000.
- **résultat** (`result`, entier). Relie un fil bleu.
