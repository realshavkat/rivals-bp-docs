---
sidebar_position: 3
title: "Ball.GroundPlace"
sidebar_label: "GroundPlace"
description: "Pose le ballon au sol devant le joueur (BALL:Spawn). 'placed' = vrai si le placement a eu lieu."
---

# GroundPlace

`Ball.GroundPlace`

Pose le ballon au sol devant le joueur (BALL:Spawn). 'placed' = vrai si le placement a eu lieu.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| ball | `ball` | entité |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| placed | `placed` | oui/non |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **ball** (`ball`, entité). Relie un fil bleu.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **placed** (`placed`, oui/non). Relie un fil bleu.
