---
sidebar_position: 2
title: "Status.Clear"
sidebar_label: "Clear"
description: "Termine tout de suite le statut posé sur la cible par CETTE exécution (ex. fin anticipée d'une immunité)."
---

# Clear

`Status.Clear`

Termine tout de suite le statut posé sur la cible par CETTE exécution (ex. fin anticipée d'une immunité).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| cible | `target` | joueur |  |  |
| status | `status` | texte | `dribble_immune` | écrit dans le bloc, choix: `slow`, `root`, `stun`, `dribble_immune` |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| cleared | `cleared` | entier |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **cible** (`target`, joueur). Relie un fil bleu.
- **status** (`status`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `dribble_immune`. Valeurs prévues: `slow`, `root`, `stun`, `dribble_immune`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **cleared** (`cleared`, entier). Relie un fil bleu.
