---
sidebar_position: 9
title: "Event.OnKeyRelease"
sidebar_label: "OnKeyRelease"
description: "OnKeyRelease"
---

# OnKeyRelease

`Event.OnKeyRelease`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Il se réveille sur l'événement `OnKeyRelease`.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| key | `key` | texte |  | écrit dans le bloc, choix: `attack`, `attack2`, `jump`, `duck`, `use`, `reload`, `forward`, `back`, `moveleft`, `moveright`, `speed`, `walk` |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| joueur | `player` | joueur |  |  |

## Détail

- **key** (`key`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Valeurs prévues: `attack`, `attack2`, `jump`, `duck`, `use`, `reload`, `forward`, `back`, `moveleft`, `moveright`, `speed`, `walk`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **joueur** (`player`, joueur). Relie un fil bleu.
