---
sidebar_position: 1
title: "Logic.And"
sidebar_label: "And"
description: "And"
---

# And

`Logic.And`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Logic.And(a = true, b = true)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| a | `a` | oui/non |  |  |
| b | `b` | oui/non |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | oui/non |  |  |

## Détail

- **a** (`a`, oui/non). Relie un fil bleu.
- **b** (`b`, oui/non). Relie un fil bleu.
- **résultat** (`result`, oui/non). Relie un fil bleu.
