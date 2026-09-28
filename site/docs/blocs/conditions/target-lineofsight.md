---
sidebar_position: 12
title: "Target.LineOfSight"
sidebar_label: "LineOfSight"
description: "LineOfSight"
---

# LineOfSight

`Target.LineOfSight`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

Chaque passage consomme **4** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Target.LineOfSight(from = {0, 0, 0}, to = {0, 0, 0})
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| from | `from` | vecteur |  |  |
| to | `to` | vecteur |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| visible | `visible` | oui/non |  |  |

## Détail

- **from** (`from`, vecteur). Relie un fil bleu.
- **to** (`to`, vecteur). Relie un fil bleu.
- **visible** (`visible`, oui/non). Relie un fil bleu.
