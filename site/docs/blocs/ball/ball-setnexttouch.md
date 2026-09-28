---
sidebar_position: 10
title: "Ball.SetNextTouch"
sidebar_label: "SetNextTouch"
description: "Empêche une entité (ballon ou joueur) de toucher/reprendre le ballon pendant N secondes."
---

# SetNextTouch

`Ball.SetNextTouch`

Empêche une entité (ballon ou joueur) de toucher/reprendre le ballon pendant N secondes.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| cible | `entity` | entité |  |  |
| secondes | `seconds` | nombre | `0.2` | de 0 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **cible** (`entity`, entité). Relie un fil bleu.
- **secondes** (`seconds`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.2`. Borné de 0 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
