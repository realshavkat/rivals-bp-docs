---
sidebar_position: 8
title: "Ball.Release"
sidebar_label: "Release"
description: "Le joueur lâche son ballon (RemoveSoccer) sans le frapper. Os d'attache remis à ''."
---

# Release

`Ball.Release`

Le joueur lâche son ballon (RemoveSoccer) sans le frapper. Os d'attache remis à ''.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`release_ball`](/langage/verbes#release_ball).

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **3** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| hideClient | `hideClient` | oui/non | `non` |  |
| nextTouch | `nextTouch` | nombre | `0.2` | de 0 à 5 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| ball | `ball` | entité |  |  |
| released | `released` | oui/non |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **hideClient** (`hideClient`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **nextTouch** (`nextTouch`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.2`. Borné de 0 à 5.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **ball** (`ball`, entité). Relie un fil bleu.
- **released** (`released`, oui/non). Relie un fil bleu.
