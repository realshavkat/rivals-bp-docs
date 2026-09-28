---
sidebar_position: 13
title: "Event.OnTackleAttempt"
sidebar_label: "OnTackleAttempt"
description: "Le lanceur tente un tacle (hook du gamemode BL::Otoya::TackleAttempt, émis à chaque tentative)."
---

# OnTackleAttempt

`Event.OnTackleAttempt`

Le lanceur tente un tacle (hook du gamemode BL::Otoya::TackleAttempt, émis à chaque tentative).

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Il se réveille sur l'événement `OnTackleAttempt`.

## Entrées

Aucune.

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| joueur | `player` | joueur |  |  |

## Détail

- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **joueur** (`player`, joueur). Relie un fil bleu.
