---
sidebar_position: 1
title: "Movement.ApplyVelocity"
sidebar_label: "ApplyVelocity"
description: "Ajoute (add) ou remplace (set) la vélocité d'une entité. Norme bornée à 4000."
---

# Ajoute (add) ou remplace (set) la vélocité d'une entité. Norme bornée à 4000

`Movement.ApplyVelocity`

Ajoute (add) ou remplace (set) la vélocité d'une entité. Norme bornée à 4000.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| cible | `target` | entité |  |  |
| velocity | `velocity` | vecteur |  |  |
| cible | `mode` | texte | `add` | écrit dans le bloc, choix: `add`, `set` |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **cible** (`target`, entité). Relie un fil bleu.
- **velocity** (`velocity`, vecteur). Relie un fil bleu.
- **cible** (`mode`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `add`. Valeurs prévues: `add`, `set`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
