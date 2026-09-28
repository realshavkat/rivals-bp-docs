---
sidebar_position: 13
title: "Vector.Sub"
sidebar_label: "Sub"
description: "Sub"
---

# Sub

`Vector.Sub`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Vector.Sub(a = {0, 0, 0}, b = {0, 0, 0})
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| a | `a` | vecteur |  |  |
| b | `b` | vecteur |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | vecteur |  |  |

## Détail

- **a** (`a`, vecteur). Relie un fil bleu.
- **b** (`b`, vecteur). Relie un fil bleu.
- **résultat** (`result`, vecteur). Relie un fil bleu.
