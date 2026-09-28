---
sidebar_position: 1
title: "Entity.SpawnProjectile"
sidebar_label: "SpawnProjectile"
description: "Prop physique temporaire (max 8 par exécution), supprimé après 'lifetime'."
---

# Prop physique temporaire (max 8 par exécution), supprimé après 'lifetime'

`Entity.SpawnProjectile`

Prop physique temporaire (max 8 par exécution), supprimé après 'lifetime'.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **10** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| model | `model` | texte |  | écrit dans le bloc |
| pos | `pos` | vecteur |  |  |
| velocity | `velocity` | vecteur |  | optionnel |
| lifetime | `lifetime` | nombre | `3` | de 0.1 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| cible | `entity` | entité |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **model** (`model`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **pos** (`pos`, vecteur). Relie un fil bleu.
- **velocity** (`velocity`, vecteur). Le fil peut rester vide.
- **lifetime** (`lifetime`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `3`. Borné de 0.1 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **cible** (`entity`, entité). Relie un fil bleu.
