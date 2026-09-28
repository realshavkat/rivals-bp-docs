---
sidebar_position: 8
title: "Math.Max"
sidebar_label: "Max"
description: "Le plus grand des deux nombres."
---

# Le plus grand des deux nombres

`Math.Max`

Le plus grand des deux nombres.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Math.Max(a = 0, b = 0)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| a | `a` | nombre | `0` | de -1000000 à 1000000 |
| b | `b` | nombre | `0` | de -1000000 à 1000000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | nombre |  |  |

## Détail

- **a** (`a`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **b** (`b`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **résultat** (`result`, nombre). Relie un fil bleu.
