---
sidebar_position: 1
title: "Flow.Branch"
sidebar_label: "Branch"
description: "si oui, ou si non"
---

# Si oui, ou si non

`Flow.Branch`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Enchaînement. Il décide quelle suite blanche part, et quand.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| condition | `condition` | oui/non |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| oui | `true` | flux |  |  |
| non | `false` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **condition** (`condition`, oui/non). Relie un fil bleu.
- **oui** (`true`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **non** (`false`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
