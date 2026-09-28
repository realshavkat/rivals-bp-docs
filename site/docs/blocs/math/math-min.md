---
sidebar_position: 9
title: "Math.Min"
sidebar_label: "Min"
description: "Le plus petit des deux nombres."
---

# Le plus petit des deux nombres

`Math.Min`

Le plus petit des deux nombres.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Math.Min(a = 0, b = 0)
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
