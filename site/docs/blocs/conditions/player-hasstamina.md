---
sidebar_position: 4
title: "Player.HasStamina"
sidebar_label: "HasStamina"
description: "HasStamina"
---

# HasStamina

`Player.HasStamina`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Player.HasStamina(player = caster, amount = 10)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |
| amount | `amount` | nombre | `10` | de 0 à 1000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | oui/non |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **amount** (`amount`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `10`. Borné de 0 à 1000.
- **résultat** (`result`, oui/non). Relie un fil bleu.
