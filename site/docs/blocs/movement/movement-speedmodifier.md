---
sidebar_position: 8
title: "Movement.SpeedModifier"
sidebar_label: "SpeedModifier"
description: "Multiplie la vitesse de marche/course pendant 'duration'. Les modificateurs se cumulent correctement."
---

# SpeedModifier

`Movement.SpeedModifier`

Multiplie la vitesse de marche/course pendant 'duration'. Les modificateurs se cumulent correctement.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Dans la vue Code, le verbe est [`speed`](/langage/verbes#speed) : `speed(multiplier, duration)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| multiplier | `multiplier` | nombre | `1.5` |  |
| durée | `duration` | nombre | `1` | de 0.05 à … |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **multiplier** (`multiplier`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1.5`.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.05 à ….
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
