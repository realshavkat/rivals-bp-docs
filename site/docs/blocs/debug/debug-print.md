---
sidebar_position: 1
title: "Debug.Print"
sidebar_label: "Print"
description: "Affiche une valeur dans la trace rbp_debug (aucun effet sinon)."
---

# Affiche une valeur dans la trace rbp_debug (aucun effet sinon)

`Debug.Print`

Affiche une valeur dans la trace rbp_debug (aucun effet sinon).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| texte | `text` | texte | `vide` |  |
| valeur | `value` | quelconque |  | optionnel |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **texte** (`text`, texte). Sans fil bleu, le défaut est utilisé. Défaut: `vide`.
- **valeur** (`value`, quelconque). Le fil peut rester vide.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
