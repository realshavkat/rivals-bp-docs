---
sidebar_position: 6
title: "Player.CamLock"
sidebar_label: "CamLock"
description: "Verrouille la caméra du joueur pendant 'duration' (toujours déverrouillée à la fin)."
---

# CamLock

`Player.CamLock`

Verrouille la caméra du joueur pendant 'duration' (toujours déverrouillée à la fin).

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| durée | `duration` | nombre | `1` | de 0.02 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.02 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
