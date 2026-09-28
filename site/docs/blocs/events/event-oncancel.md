---
sidebar_position: 4
title: "Event.OnCancel"
sidebar_label: "OnCancel"
description: "L'exécution est annulée (mort, déconnexion, stun, erreur...). Rien ne peut être planifié ici."
---

# OnCancel

`Event.OnCancel`

L'exécution est annulée (mort, déconnexion, stun, erreur...). Rien ne peut être planifié ici.

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Il se réveille sur l'événement `OnCancel`.

## Entrées

Aucune.

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| reason | `reason` | texte |  |  |

## Détail

- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **reason** (`reason`, texte). Relie un fil bleu.
