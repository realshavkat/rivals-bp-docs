---
sidebar_position: 7
title: "FX.ScreenShake"
sidebar_label: "ScreenShake"
description: "Secousse de caméra."
---

# Secousse de caméra

`FX.ScreenShake`

Secousse de caméra.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`shake`](/langage/verbes#shake) : `shake(pos)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| pos | `pos` | vecteur |  |  |
| force caméra | `amplitude` | nombre | `5` | de 0 à 255 |
| frequency | `frequency` | nombre | `5` | de 0 à 255 |
| durée | `duration` | nombre | `0.5` | de 0 à 10 |
| radius | `radius` | nombre | `512` | de 0 à 4000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **pos** (`pos`, vecteur). Relie un fil bleu.
- **force caméra** (`amplitude`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `5`. Borné de 0 à 255.
- **frequency** (`frequency`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `5`. Borné de 0 à 255.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.5`. Borné de 0 à 10.
- **radius** (`radius`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `512`. Borné de 0 à 4000.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
