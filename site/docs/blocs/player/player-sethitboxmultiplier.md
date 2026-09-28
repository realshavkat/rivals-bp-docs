---
sidebar_position: 17
title: "Player.SetHitboxMultiplier"
sidebar_label: "SetHitboxMultiplier"
description: "Agrandit la hitbox du joueur pendant 'duration' (remise à 1 ensuite, même si l'exécution est annulée)."
---

# SetHitboxMultiplier

`Player.SetHitboxMultiplier`

Agrandit la hitbox du joueur pendant 'duration' (remise à 1 ensuite, même si l'exécution est annulée).

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Dans la vue Code, le verbe est [`hitbox`](/langage/verbes#hitbox) : `hitbox(value, duration)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    hitbox(1.5, 1, player = caster)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| valeur | `value` | nombre | `1.5` | de 0.1 à 5 |
| durée | `duration` | nombre | `1` | de 0.05 à … |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **valeur** (`value`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1.5`. Borné de 0.1 à 5.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.05 à ….
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
