---
sidebar_position: 16
title: "Player.SetHitboxModel"
sidebar_label: "SetHitboxModel"
description: "Change le modèle d'une hitbox du joueur (ex. hitbox de gardien) puis restaure 'restoreModel'."
---

# SetHitboxModel

`Player.SetHitboxModel`

Change le modèle d'une hitbox du joueur (ex. hitbox de gardien) puis restaure 'restoreModel'.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| kind | `kind` | texte | `goal` | écrit dans le bloc, choix: `goal`, `player`, `player_torso` |
| model | `model` | texte |  | écrit dans le bloc |
| restoreModel | `restoreModel` | texte |  | écrit dans le bloc |
| durée | `duration` | nombre | `1` | de 0.05 à … |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| found | `found` | oui/non |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **kind** (`kind`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `goal`. Valeurs prévues: `goal`, `player`, `player_torso`.
- **model** (`model`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **restoreModel** (`restoreModel`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.05 à ….
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **found** (`found`, oui/non). Relie un fil bleu.
