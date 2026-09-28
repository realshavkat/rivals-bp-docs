---
sidebar_position: 1
title: "Angle.Forward"
sidebar_label: "Forward"
description: "Forward"
---

# Forward

`Angle.Forward`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Angle.Forward()
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| angle | `angle` | angle |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| forward | `forward` | vecteur |  |  |

## Détail

- **angle** (`angle`, angle). Relie un fil bleu.
- **forward** (`forward`, vecteur). Relie un fil bleu.
