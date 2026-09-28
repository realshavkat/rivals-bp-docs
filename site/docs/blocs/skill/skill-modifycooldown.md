---
sidebar_position: 3
title: "Skill.ModifyCooldown"
sidebar_label: "ModifyCooldown"
description: "Multiplie le temps de recharge RESTANT d'une technique du joueur."
---

# Multiplie le temps de recharge RESTANT d'une technique du joueur

`Skill.ModifyCooldown`

Multiplie le temps de recharge RESTANT d'une technique du joueur.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| skillId | `skillId` | texte |  |  |
| multiplier | `multiplier` | nombre | `0.5` | de 0 à 1 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| remaining | `remaining` | nombre |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **skillId** (`skillId`, texte). Relie un fil bleu.
- **multiplier** (`multiplier`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.5`. Borné de 0 à 1.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **remaining** (`remaining`, nombre). Relie un fil bleu.
