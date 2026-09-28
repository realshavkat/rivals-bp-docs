---
sidebar_position: 1
title: "Rules.StealAlwaysReady"
sidebar_label: "StealAlwaysReady"
description: "Pendant 'duration' (ou jusqu'à 'stop'), les tentatives de vol du joueur ne sont plus limitées par le délai entre deux vols."
---

# StealAlwaysReady

`Rules.StealAlwaysReady`

Pendant 'duration' (ou jusqu'à 'stop'), les tentatives de vol du joueur ne sont plus limitées par le délai entre deux vols.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| stop | `stop` | flux |  |  |
| joueur | `player` | joueur |  |  |
| durée | `duration` | nombre | `6` | de 0.05 à … |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **stop** (`stop`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `6`. Borné de 0.05 à ….
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
