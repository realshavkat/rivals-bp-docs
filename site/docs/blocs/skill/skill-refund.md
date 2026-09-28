---
sidebar_position: 4
title: "Skill.Refund"
sidebar_label: "Refund"
description: "Rembourse la stamina et annule le cooldown de la technique en cours (ex. aucune cible)."
---

# Refund

`Skill.Refund`

Rembourse la stamina et annule le cooldown de la technique en cours (ex. aucune cible).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`refund`](/langage/verbes#refund).

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Présent seulement sur: technique.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
