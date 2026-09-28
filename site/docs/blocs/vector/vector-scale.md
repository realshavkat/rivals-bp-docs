---
sidebar_position: 12
title: "Vector.Scale"
sidebar_label: "Scale"
description: "Scale"
---

# Scale

`Vector.Scale`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Vector.Scale(vector = {0, 0, 0}, scale = 1)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| vector | `vector` | vecteur |  |  |
| scale | `scale` | nombre | `1` | de -1000000 à 1000000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | vecteur |  |  |

## Détail

- **vector** (`vector`, vecteur). Relie un fil bleu.
- **scale** (`scale`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de -1000000 à 1000000.
- **résultat** (`result`, vecteur). Relie un fil bleu.
