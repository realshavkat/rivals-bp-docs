---
sidebar_position: 5
title: "Vector.AdjustZ"
sidebar_label: "AdjustZ"
description: "z = clamp(z + add, min, max), puis normalisation optionnelle."
---

# Z = clamp(z + add, min, max), puis normalisation optionnelle

`Vector.AdjustZ`

z = clamp(z + add, min, max), puis normalisation optionnelle.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| vector | `vector` | vecteur |  |  |
| add | `add` | nombre | `0` | de … à 1000000 |
| min | `min` | nombre |  | de … à 1000000 |
| max | `max` | nombre |  | de … à 1000000 |
| normalize | `normalize` | oui/non | `non` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | vecteur |  |  |

## Détail

- **vector** (`vector`, vecteur). Relie un fil bleu.
- **add** (`add`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de … à 1000000.
- **min** (`min`, nombre). Relie un fil bleu. Borné de … à 1000000.
- **max** (`max`, nombre). Relie un fil bleu. Borné de … à 1000000.
- **normalize** (`normalize`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **résultat** (`result`, vecteur). Relie un fil bleu.
