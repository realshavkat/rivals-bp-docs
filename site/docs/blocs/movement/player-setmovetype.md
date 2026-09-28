---
sidebar_position: 17
title: "Player.SetMoveType"
sidebar_label: "SetMoveType"
description: "none : le joueur ne bouge plus (sans le figer) ; walk : mouvement normal. Toujours remis à walk à la fin de l'exécution."
---

# SetMoveType

`Player.SetMoveType`

none : le joueur ne bouge plus (sans le figer) ; walk : mouvement normal. Toujours remis à walk à la fin de l'exécution.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Player.SetMoveType(player = caster, mode = "none")
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| cible | `mode` | texte | `none` | écrit dans le bloc, choix: `none`, `walk` |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **cible** (`mode`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `none`. Valeurs prévues: `none`, `walk`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
