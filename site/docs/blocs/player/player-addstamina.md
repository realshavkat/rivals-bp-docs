---
sidebar_position: 4
title: "Player.AddStamina"
sidebar_label: "AddStamina"
description: "AddStamina"
---

# AddStamina

`Player.AddStamina`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Player.AddStamina(player = caster, amount = 10)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| amount | `amount` | nombre | `10` | de 0 à 1000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **amount** (`amount`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `10`. Borné de 0 à 1000.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
