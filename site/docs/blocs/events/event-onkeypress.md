---
sidebar_position: 8
title: "Event.OnKeyPress"
sidebar_label: "OnKeyPress"
description: "Le lanceur appuie sur une touche pendant que l'exécution est vivante."
---

# Le lanceur appuie sur une touche pendant que l'exécution est vivante

`Event.OnKeyPress`

Le lanceur appuie sur une touche pendant que l'exécution est vivante.

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Il se réveille sur l'événement `OnKeyPress`.

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
