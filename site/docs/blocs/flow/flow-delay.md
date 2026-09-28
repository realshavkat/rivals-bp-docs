---
sidebar_position: 5
title: "Flow.Delay"
sidebar_label: "Delay"
description: "Attend N secondes."
---

# Attendre

`Flow.Delay`

Attend N secondes.

Enchaînement. Il décide quelle suite blanche part, et quand.

Dans la vue Code, le verbe est [`wait`](/langage/verbes#wait) : `wait(seconds)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| secondes | `seconds` | nombre | `0.2` | de 0 à … |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **secondes** (`seconds`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.2`. Borné de 0 à ….
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
