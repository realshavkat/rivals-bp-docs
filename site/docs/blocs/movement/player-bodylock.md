---
sidebar_position: 11
title: "Player.BodyLock"
sidebar_label: "BodyLock"
description: "Verrouille l'orientation du corps sur la visée actuelle (système de mouvement BL.RivalsMove, sans effet s'il est absent). 'stop' déverrouille."
---

# BodyLock

`Player.BodyLock`

Verrouille l'orientation du corps sur la visée actuelle (système de mouvement BL.RivalsMove, sans effet s'il est absent). 'stop' déverrouille.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Player.BodyLock(player = caster, duration = 1)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| stop | `stop` | flux |  |  |
| joueur | `player` | joueur |  |  |
| durée | `duration` | nombre | `1` | de 0.05 à … |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **stop** (`stop`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.05 à ….
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
