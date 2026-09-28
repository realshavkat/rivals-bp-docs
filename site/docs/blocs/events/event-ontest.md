---
sidebar_position: 14
title: "Event.OnTest"
sidebar_label: "OnTest"
description: "OnTest"
---

# OnTest

`Event.OnTest`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Présent seulement sur: test.

Il se réveille sur l'événement `OnTest`.

## Entrées

Aucune.

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| a | `a` | quelconque |  |  |

## Détail

- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **a** (`a`, quelconque). Relie un fil bleu.
