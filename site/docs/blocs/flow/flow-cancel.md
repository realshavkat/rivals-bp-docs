---
sidebar_position: 3
title: "Flow.Cancel"
sidebar_label: "Cancel"
description: "Termine immédiatement l'exécution (les nettoyages sont lancés)."
---

# Termine immédiatement l'exécution (les nettoyages sont lancés)

`Flow.Cancel`

Termine immédiatement l'exécution (les nettoyages sont lancés).

Enchaînement. Il décide quelle suite blanche part, et quand.

Dans la vue Code, le verbe est [`cancel`](/langage/verbes#cancel) : `cancel(reason)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| reason | `reason` | texte | `Flow.Cancel` | écrit dans le bloc |

## Sorties

Aucune.

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **reason** (`reason`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `Flow.Cancel`.
