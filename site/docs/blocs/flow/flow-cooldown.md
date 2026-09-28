---
sidebar_position: 4
title: "Flow.Cooldown"
sidebar_label: "Cooldown"
description: "Laisse passer au plus une fois toutes les N secondes (par exécution ou par joueur)."
---

# Cooldown

`Flow.Cooldown`

Laisse passer au plus une fois toutes les N secondes (par exécution ou par joueur).

Enchaînement. Il décide quelle suite blanche part, et quand.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| secondes | `seconds` | nombre | `1` | de 0 à 600 |
| scope | `scope` | texte | `run` | écrit dans le bloc, choix: `run`, `player` |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| ready | `ready` | flux |  |  |
| blocked | `blocked` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **secondes** (`seconds`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0 à 600.
- **scope** (`scope`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `run`. Valeurs prévues: `run`, `player`.
- **ready** (`ready`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **blocked** (`blocked`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
