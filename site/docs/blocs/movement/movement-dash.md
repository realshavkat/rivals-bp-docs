---
sidebar_position: 2
title: "Movement.Dash"
sidebar_label: "Dash"
description: "Dash du gamemode (PLAYER:Dash) dans une direction relative."
---

# Dash

`Movement.Dash`

Dash du gamemode (PLAYER:Dash) dans une direction relative.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Movement.Dash(player = caster, direction = "forward", speed = 600, duration = 0.2)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| direction | `direction` | texte | `forward` | choix: `forward`, `back`, `left`, `right`, `forward_left`, `forward_right`, `forward_moveright`, `back_moveright` |
| vitesse | `speed` | nombre | `600` | de 0 à 3000 |
| durée | `duration` | nombre | `0.2` | de 0.05 à 3 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **direction** (`direction`, texte). Sans fil bleu, le défaut est utilisé. Défaut: `forward`. Valeurs prévues: `forward`, `back`, `left`, `right`, `forward_left`, `forward_right`, `forward_moveright`, `back_moveright`.
- **vitesse** (`speed`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `600`. Borné de 0 à 3000.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.2`. Borné de 0.05 à 3.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
