---
sidebar_position: 6
title: "Movement.Lock"
sidebar_label: "Lock"
description: "Bloque les déplacements (verrou existant du gamemode, prédit)."
---

# Bloque les déplacements (verrou existant du gamemode, prédit)

`Movement.Lock`

Bloque les déplacements (verrou existant du gamemode, prédit).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`lock`](/langage/verbes#lock) : `lock(duration)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| durée | `duration` | nombre | `0.5` | de 0.05 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.5`. Borné de 0.05 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
