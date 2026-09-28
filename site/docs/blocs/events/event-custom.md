---
sidebar_position: 1
title: "Event.Custom"
sidebar_label: "Custom"
description: "Événement nommé, déclenché par Flow.CallEvent dans le même graphe."
---

# Événement nommé, déclenché par Flow.CallEvent dans le même graphe

`Event.Custom`

Événement nommé, déclenché par Flow.CallEvent dans le même graphe.

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Il se réveille sur l'événement `Custom`.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| nom | `name` | texte |  | écrit dans le bloc |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| a | `a` | quelconque |  |  |
| b | `b` | quelconque |  |  |

## Détail

- **nom** (`name`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **a** (`a`, quelconque). Relie un fil bleu.
- **b** (`b`, quelconque). Relie un fil bleu.
