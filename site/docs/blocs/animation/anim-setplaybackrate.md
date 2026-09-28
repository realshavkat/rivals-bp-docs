---
sidebar_position: 4
title: "Anim.SetPlaybackRate"
sidebar_label: "SetPlaybackRate"
description: "SetPlaybackRate"
---

# SetPlaybackRate

`Anim.SetPlaybackRate`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| rythme | `rate` | nombre | `1` | de 0 à 5 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **rythme** (`rate`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0 à 5.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
