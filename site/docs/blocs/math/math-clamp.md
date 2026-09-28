---
sidebar_position: 4
title: "Math.Clamp"
sidebar_label: "Clamp"
description: "Clamp"
---

# Clamp

`Math.Clamp`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Math.Clamp(value = 0, min = 0, max = 1)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| valeur | `value` | nombre | `0` | de -1000000 à 1000000 |
| min | `min` | nombre | `0` | de -1000000 à 1000000 |
| max | `max` | nombre | `1` | de -1000000 à 1000000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | nombre |  |  |

## Détail

- **valeur** (`value`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **min** (`min`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -1000000 à 1000000.
- **max** (`max`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de -1000000 à 1000000.
- **résultat** (`result`, nombre). Relie un fil bleu.
