---
sidebar_position: 6
title: "Vector.Break"
sidebar_label: "Break"
description: "Break"
---

# Break

`Vector.Break`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Vector.Break(vector = {0, 0, 0})
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| vector | `vector` | vecteur |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| x | `x` | nombre |  |  |
| y | `y` | nombre |  |  |
| z | `z` | nombre |  |  |

## Détail

- **vector** (`vector`, vecteur). Relie un fil bleu.
- **x** (`x`, nombre). Relie un fil bleu.
- **y** (`y`, nombre). Relie un fil bleu.
- **z** (`z`, nombre). Relie un fil bleu.
