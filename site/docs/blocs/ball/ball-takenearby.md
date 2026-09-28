---
sidebar_position: 17
title: "Ball.TakeNearby"
sidebar_label: "TakeNearby"
description: "Ramasse le ballon libre le plus proche dans un rayon."
---

# Ramasse le ballon libre le plus proche dans un rayon

`Ball.TakeNearby`

Ramasse le ballon libre le plus proche dans un rayon.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`take_ball`](/langage/verbes#take_ball) : `take_ball(radius)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **5** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| radius | `radius` | nombre | `100` | de 8 à 400 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| taken | `taken` | oui/non |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **radius** (`radius`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `100`. Borné de 8 à 400.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **taken** (`taken`, oui/non). Relie un fil bleu.
