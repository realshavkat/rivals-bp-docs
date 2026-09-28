---
sidebar_position: 16
title: "Player.SetGravity"
sidebar_label: "SetGravity"
description: "SetGravity"
---

# SetGravity

`Player.SetGravity`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Player.SetGravity(player = caster, gravity = 0.9, duration = 1)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| gravity | `gravity` | nombre | `0.9` | de 0 à 3 |
| durée | `duration` | nombre | `1` | de 0.02 à … |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **gravity** (`gravity`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.9`. Borné de 0 à 3.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.02 à ….
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
