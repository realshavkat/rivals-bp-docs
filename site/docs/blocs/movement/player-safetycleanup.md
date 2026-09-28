---
sidebar_position: 15
title: "Player.SafetyCleanup"
sidebar_label: "SafetyCleanup"
description: "Filet de sécurité existant : rend le contrôle après 'delay' si le joueur est resté bloqué."
---

# SafetyCleanup

`Player.SafetyCleanup`

Filet de sécurité existant : rend le contrôle après 'delay' si le joueur est resté bloqué.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| delay | `delay` | nombre | `2` | de 0.1 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **delay** (`delay`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `2`. Borné de 0.1 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
