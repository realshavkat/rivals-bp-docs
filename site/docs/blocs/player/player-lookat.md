---
sidebar_position: 11
title: "Player.LookAt"
sidebar_label: "LookAt"
description: "Oriente la vue du joueur vers une position (tangage conservé si keepPitch)."
---

# Oriente la vue du joueur vers une position (tangage conservé si keepPitch)

`Player.LookAt`

Oriente la vue du joueur vers une position (tangage conservé si keepPitch).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| pos | `pos` | vecteur |  |  |
| keepPitch | `keepPitch` | oui/non | `oui` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **pos** (`pos`, vecteur). Relie un fil bleu.
- **keepPitch** (`keepPitch`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
