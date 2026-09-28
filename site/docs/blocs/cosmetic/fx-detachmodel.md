---
sidebar_position: 4
title: "FX.DetachModel"
sidebar_label: "DetachModel"
description: "Retire un modèle attaché par FX.AttachModel (PLAYER:UnParentModel)."
---

# Retire un modèle attaché par FX.AttachModel (PLAYER:UnParentModel)

`FX.DetachModel`

Retire un modèle attaché par FX.AttachModel (PLAYER:UnParentModel).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| model | `model` | texte |  | écrit dans le bloc |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **model** (`model`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
