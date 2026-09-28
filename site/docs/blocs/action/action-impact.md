---
sidebar_position: 3
title: "Action.Impact"
sidebar_label: "Impact"
description: "Tir complet. Animation, attente, frappe, effet et caméra dans un seul bloc."
---

# Tir complet en un bloc

`Action.Impact`

Tir complet. Animation, attente, frappe, effet et caméra dans un seul bloc.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Dans la vue Code, le verbe est [`impact`](/langage/verbes#impact) : `impact(power)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **5** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  | optionnel |
| animation | `sequence` | texte | `player_shoot_highpower_v0_bton` |  |
| attente | `windup` | nombre | `0.4` | de 0 à 3 |
| puissance | `power` | nombre | `12000` | de 0 à 100000 |
| hauteur | `lift` | nombre | `220` | de -5000 à 5000 |
| particule | `particle` | texte | `vide` | optionnel, écrit dans le bloc |
| son | `sound` | texte | `vide` | optionnel, écrit dans le bloc |
| caméra | `shake` | oui/non | `oui` |  |
| force caméra | `amplitude` | nombre | `6` | de 0 à 20 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| fini | `finished` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Tu peux laisser le fil vide: le bloc prend le lanceur.
- **animation** (`sequence`, texte). Sans fil bleu, le défaut est utilisé. Défaut: `player_shoot_highpower_v0_bton`.
- **attente** (`windup`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.4`. Borné de 0 à 3.
- **puissance** (`power`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `12000`. Borné de 0 à 100000.
- **hauteur** (`lift`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `220`. Borné de -5000 à 5000.
- **particule** (`particle`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `vide`.
- **son** (`sound`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `vide`.
- **caméra** (`shake`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **force caméra** (`amplitude`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `6`. Borné de 0 à 20.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **fini** (`finished`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
