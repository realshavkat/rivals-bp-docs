---
sidebar_position: 2
title: "Balance.LevelCurve"
sidebar_label: "LevelCurve"
description: "Lerp min->max selon le niveau (1-maxLevel)."
---

# Lerp min->max selon le niveau (1-maxLevel)

`Balance.LevelCurve`

Lerp min->max selon le niveau (1-maxLevel).

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Balance.LevelCurve(level = 1, maxLevel = 5, min = 0, max = 1)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| niveau | `level` | nombre | `1` | de 1 à 20 |
| maxLevel | `maxLevel` | nombre | `5` | de 1 à 20 |
| min | `min` | nombre | `0` | de -1000000 à 1000000 |
| max | `max` | nombre | `1` | de -1000000 à 1000000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| valeur | `value` | nombre |  |  |

## Détail

- **niveau** (`level`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 1 à 20.
- **maxLevel** (`maxLevel`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `5`. Borné de 1 à 20.
- **min** (`min`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **max** (`max`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de -1000000 à 1000000.
- **valeur** (`value`, nombre). Relie un fil bleu.
