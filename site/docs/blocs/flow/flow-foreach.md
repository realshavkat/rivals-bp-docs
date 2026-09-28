---
sidebar_position: 8
title: "Flow.ForEach"
sidebar_label: "ForEach"
description: "Parcourt une liste (ex. sortie de Target.FindInSphere), max 64 éléments."
---

# Parcourt une liste (ex. sortie de Target.FindInSphere), max 64 éléments

`Flow.ForEach`

Parcourt une liste (ex. sortie de Target.FindInSphere), max 64 éléments.

Enchaînement. Il décide quelle suite blanche part, et quand.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **2** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| list | `list` | liste |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| body | `body` | flux |  |  |
| element | `element` | quelconque |  |  |
| index | `index` | entier |  |  |
| completed | `completed` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **list** (`list`, liste). Relie un fil bleu.
- **body** (`body`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **element** (`element`, quelconque). Relie un fil bleu.
- **index** (`index`, entier). Relie un fil bleu.
- **completed** (`completed`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
