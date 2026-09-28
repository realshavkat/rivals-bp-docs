---
sidebar_position: 2
title: "Anim.Play"
sidebar_label: "Play"
description: "Joue une animation."
---

# Jouer une animation

`Anim.Play`

Joue une animation.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`anim`](/langage/verbes#anim) : `anim(sequence)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| animation | `sequence` | texte |  |  |
| rythme | `rate` | nombre | `1` | de 0.05 à 5 |
| loop | `loop` | oui/non | `non` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| durée | `duration` | nombre |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **animation** (`sequence`, texte). Relie un fil bleu.
- **rythme** (`rate`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.05 à 5.
- **loop** (`loop`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **durée** (`duration`, nombre). Relie un fil bleu.
