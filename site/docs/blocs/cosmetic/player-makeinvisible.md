---
sidebar_position: 14
title: "Player.MakeInvisible"
sidebar_label: "MakeInvisible"
description: "Rend le joueur translucide pendant 'duration' (version sûre de MakeInvisibile)."
---

# Rend le joueur translucide pendant 'duration' (version sûre de MakeInvisibile)

`Player.MakeInvisible`

Rend le joueur translucide pendant 'duration' (version sûre de MakeInvisibile).

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| alpha | `alpha` | entier | `100` | de 0 à 255 |
| durée | `duration` | nombre | `0.4` | de 0.02 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **alpha** (`alpha`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `100`. Borné de 0 à 255.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.4`. Borné de 0.02 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
