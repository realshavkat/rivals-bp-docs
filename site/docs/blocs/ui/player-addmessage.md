---
sidebar_position: 1
title: "Player.AddMessage"
sidebar_label: "AddMessage"
description: "AddMessage"
---

# AddMessage

`Player.AddMessage`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| texte | `text` | texte |  | écrit dans le bloc |
| durée | `duration` | nombre | `3` | de 0.5 à 10 |
| code | `code` | entier | `1` | de 0 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **texte** (`text`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `3`. Borné de 0.5 à 10.
- **code** (`code`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
