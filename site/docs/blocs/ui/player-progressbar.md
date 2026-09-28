---
sidebar_position: 5
title: "Player.ProgressBar"
sidebar_label: "ProgressBar"
description: "ProgressBar"
---

# ProgressBar

`Player.ProgressBar`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| texte | `text` | texte |  | écrit dans le bloc |
| durée | `duration` | nombre | `1` | de 0.1 à 3600 |
| r | `r` | entier |  | optionnel, de 0 à 255 |
| g | `g` | entier |  | optionnel, de 0 à 255 |
| b | `b` | entier |  | optionnel, de 0 à 255 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **texte** (`text`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.1 à 3600.
- **r** (`r`, entier). Le fil peut rester vide. Borné de 0 à 255.
- **g** (`g`, entier). Le fil peut rester vide. Borné de 0 à 255.
- **b** (`b`, entier). Le fil peut rester vide. Borné de 0 à 255.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
