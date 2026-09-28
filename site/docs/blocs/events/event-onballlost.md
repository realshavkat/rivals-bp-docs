---
sidebar_position: 2
title: "Event.OnBallLost"
sidebar_label: "OnBallLost"
description: "Le lanceur perd le ballon."
---

# Le lanceur perd le ballon

`Event.OnBallLost`

Le lanceur perd le ballon.

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Il se réveille sur l'événement `OnBallLost`.

## Entrées

Aucune.

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| ball | `ball` | entité |  |  |

## Détail

- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **ball** (`ball`, entité). Relie un fil bleu.
