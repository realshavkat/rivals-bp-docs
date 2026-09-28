---
sidebar_position: 3
title: "Target.FindInSphere"
sidebar_label: "FindInSphere"
description: "Liste (max 16) des cibles dans un rayon : joueurs ciblables, adversaires ciblables (sans coéquipiers), tous les joueurs, porteurs, ou ballons."
---

# FindInSphere

`Target.FindInSphere`

Liste (max 16) des cibles dans un rayon : joueurs ciblables, adversaires ciblables (sans coéquipiers), tous les joueurs, porteurs, ou ballons.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Dans la vue Code, le verbe est [`find_around`](/langage/verbes#find_around) : `find_around(center, radius)`.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

Chaque passage consomme **10** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = find_around({0, 0, 0}, 200, filter = "targets", max = 8)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| center | `center` | vecteur |  |  |
| radius | `radius` | nombre | `200` | de 1 à 2000 |
| filter | `filter` | texte | `targets` | écrit dans le bloc, choix: `targets`, `opponents`, `players`, `carriers`, `balls` |
| max | `max` | entier | `8` | de 1 à 16 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| list | `list` | liste |  |  |
| count | `count` | entier |  |  |
| first | `first` | entité |  |  |

## Détail

- **center** (`center`, vecteur). Relie un fil bleu.
- **radius** (`radius`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `200`. Borné de 1 à 2000.
- **filter** (`filter`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `targets`. Valeurs prévues: `targets`, `opponents`, `players`, `carriers`, `balls`.
- **max** (`max`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `8`. Borné de 1 à 16.
- **list** (`list`, liste). Relie un fil bleu.
- **count** (`count`, entier). Relie un fil bleu.
- **first** (`first`, entité). Relie un fil bleu.
