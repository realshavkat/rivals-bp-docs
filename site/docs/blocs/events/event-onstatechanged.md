---
sidebar_position: 12
title: "Event.OnStateChanged"
sidebar_label: "OnStateChanged"
description: "Un statut du lanceur change (slow, root, stun, dribble_immune)."
---

# Un statut du lanceur change (slow, root, stun, dribble_immune)

`Event.OnStateChanged`

Un statut du lanceur change (slow, root, stun, dribble_immune).

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Il se réveille sur l'événement `OnStateChanged`.

## Entrées

Aucune.

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| state | `state` | texte |  |  |
| active | `active` | oui/non |  |  |

## Détail

- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **state** (`state`, texte). Relie un fil bleu.
- **active** (`active`, oui/non). Relie un fil bleu.
