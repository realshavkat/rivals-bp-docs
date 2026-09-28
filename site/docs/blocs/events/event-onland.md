---
sidebar_position: 10
title: "Event.OnLand"
sidebar_label: "OnLand"
description: "Le lanceur touche le sol."
---

# Le lanceur touche le sol

`Event.OnLand`

Le lanceur touche le sol.

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Il se réveille sur l'événement `OnLand`.

## Entrées

Aucune.

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| vitesse | `speed` | nombre |  |  |

## Détail

- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **vitesse** (`speed`, nombre). Relie un fil bleu.
