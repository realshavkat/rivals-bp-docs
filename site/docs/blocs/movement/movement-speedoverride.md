---
sidebar_position: 9
title: "Movement.SpeedOverride"
sidebar_label: "SpeedOverride"
description: "Vitesse de marche/course absolue pendant 'duration' (la plus récente l'emporte, restauration propre)."
---

# SpeedOverride

`Movement.SpeedOverride`

Vitesse de marche/course absolue pendant 'duration' (la plus récente l'emporte, restauration propre).

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| walk | `walk` | nombre | `200` | de 1 à 5000 |
| run | `run` | nombre | `400` | de 1 à 5000 |
| durée | `duration` | nombre | `1` | de 0.02 à … |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **walk** (`walk`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `200`. Borné de 1 à 5000.
- **run** (`run`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `400`. Borné de 1 à 5000.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.02 à ….
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
