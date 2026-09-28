---
sidebar_position: 8
title: "Vector.Length"
sidebar_label: "Length"
description: "Length"
---

# Length

`Vector.Length`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Vector.Length(vector = {0, 0, 0})
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
| length | `length` | nombre |  |  |

## Détail

- **vector** (`vector`, vecteur). Relie un fil bleu.
- **length** (`length`, nombre). Relie un fil bleu.
