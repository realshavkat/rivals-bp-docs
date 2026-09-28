---
sidebar_position: 1
title: "Raichi.IntimidateFX"
sidebar_label: "IntimidateFX"
description: "Effet visuel existant de l'Intimidation de Raichi (message Raichi::Intimidate:Play)."
---

# IntimidateFX

`Raichi.IntimidateFX`

Effet visuel existant de l'Intimidation de Raichi (message Raichi::Intimidate:Play).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| cible | `target` | entité |  | optionnel |
| touche | `hit` | oui/non | `non` |  |
| durée | `duration` | nombre | `0.85` | de 0 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **cible** (`target`, entité). Le fil peut rester vide.
- **touche** (`hit`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.85`. Borné de 0 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
