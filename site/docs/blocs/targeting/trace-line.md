---
sidebar_position: 6
title: "Trace.Line"
sidebar_label: "Line"
description: "Line"
---

# Line

`Trace.Line`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

Chaque passage consomme **4** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Trace.Line(start = {0, 0, 0}, stop = {0, 0, 0})
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| start | `start` | vecteur |  |  |
| stop | `stop` | vecteur |  |  |

## Sorties

Aucune.

## Détail

- **start** (`start`, vecteur). Relie un fil bleu.
- **stop** (`stop`, vecteur). Relie un fil bleu.
