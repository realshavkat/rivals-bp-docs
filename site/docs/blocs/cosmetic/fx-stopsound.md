---
sidebar_position: 11
title: "FX.StopSound"
sidebar_label: "StopSound"
description: "Arrête un son joué par FX.Sound sur une entité (sons de Flow en boucle)."
---

# Arrête un son joué par FX.Sound sur une entité (sons de Flow en boucle)

`FX.StopSound`

Arrête un son joué par FX.Sound sur une entité (sons de Flow en boucle).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| nom | `name` | texte |  | écrit dans le bloc |
| cible | `entity` | entité |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **nom** (`name`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **cible** (`entity`, entité). Relie un fil bleu.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
