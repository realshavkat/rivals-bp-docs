---
sidebar_position: 1
title: "Status.Apply"
sidebar_label: "Apply"
description: "slow (magnitude = multiplicateur 0-1), root, stun (annule les skills de la cible), dribble_immune."
---

# Appliquer un effet

`Status.Apply`

slow (magnitude = multiplicateur 0-1), root, stun (annule les skills de la cible), dribble_immune.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Dans la vue Code, le verbe est [`apply`](/langage/verbes#apply) : `apply(target, status, duration)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| cible | `target` | joueur |  |  |
| status | `status` | texte | `slow` | choix: `slow`, `root`, `stun`, `dribble_immune` |
| durée | `duration` | nombre | `1` | de 0.05 à … |
| magnitude | `magnitude` | nombre | `0.5` | de 0 à 1 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| applied | `applied` | oui/non |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **cible** (`target`, joueur). Relie un fil bleu.
- **status** (`status`, texte). Sans fil bleu, le défaut est utilisé. Défaut: `slow`. Valeurs prévues: `slow`, `root`, `stun`, `dribble_immune`.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.05 à ….
- **magnitude** (`magnitude`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.5`. Borné de 0 à 1.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **applied** (`applied`, oui/non). Relie un fil bleu.
