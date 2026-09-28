---
sidebar_position: 11
title: "Flow.Sequence"
sidebar_label: "Sequence"
description: "Exécute then_1, then_2, then_3, then_4 dans l'ordre."
---

# Plusieurs suites

`Flow.Sequence`

Exécute then_1, then_2, then_3, then_4 dans l'ordre.

Enchaînement. Il décide quelle suite blanche part, et quand.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| then 1 | `then_1` | flux |  |  |
| then 2 | `then_2` | flux |  |  |
| then 3 | `then_3` | flux |  |  |
| then 4 | `then_4` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **then 1** (`then_1`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **then 2** (`then_2`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **then 3** (`then_3`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **then 4** (`then_4`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
