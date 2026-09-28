---
sidebar_position: 13
title: "Flow.WaitUntil"
sidebar_label: "WaitUntil"
description: "Réévalue 'condition' à intervalle régulier jusqu'à ce qu'elle soit vraie (ou timeout)."
---

# WaitUntil

`Flow.WaitUntil`

Réévalue 'condition' à intervalle régulier jusqu'à ce qu'elle soit vraie (ou timeout).

Enchaînement. Il décide quelle suite blanche part, et quand.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **2** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| condition | `condition` | oui/non |  |  |
| interval | `interval` | nombre | `0.05` | de … à 5 |
| timeout | `timeout` | nombre | `2` | de 0.05 à … |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| timeout | `timeout` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **condition** (`condition`, oui/non). Relie un fil bleu.
- **interval** (`interval`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.05`. Borné de … à 5.
- **timeout** (`timeout`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `2`. Borné de 0.05 à ….
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **timeout** (`timeout`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
