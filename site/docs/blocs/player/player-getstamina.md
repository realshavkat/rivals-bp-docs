---
sidebar_position: 10
title: "Player.GetStamina"
sidebar_label: "GetStamina"
description: "GetStamina"
---

# GetStamina

`Player.GetStamina`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Player.GetStamina(player = caster)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| stamina | `stamina` | nombre |  |  |
| max | `max` | nombre |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **stamina** (`stamina`, nombre). Relie un fil bleu.
- **max** (`max`, nombre). Relie un fil bleu.
