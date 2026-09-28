---
sidebar_position: 12
title: "Flow.SwitchInt"
sidebar_label: "SwitchInt"
description: "SwitchInt"
---

# SwitchInt

`Flow.SwitchInt`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Enchaînement. Il décide quelle suite blanche part, et quand.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| valeur | `value` | entier | `1` | de … à 1000000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| case 1 | `case_1` | flux |  |  |
| case 2 | `case_2` | flux |  |  |
| case 3 | `case_3` | flux |  |  |
| case 4 | `case_4` | flux |  |  |
| default | `default` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **valeur** (`value`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de … à 1000000.
- **case 1** (`case_1`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **case 2** (`case_2`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **case 3** (`case_3`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **case 4** (`case_4`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **default** (`default`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
