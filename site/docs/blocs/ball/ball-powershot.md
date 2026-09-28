---
sidebar_position: 7
title: "Ball.PowerShot"
sidebar_label: "PowerShot"
description: "Tir puissant du Skill Kit (ReleasePowerShot). 'released' se déclenche quand le ballon part."
---

# Frapper la balle

`Ball.PowerShot`

Tir puissant du Skill Kit (ReleasePowerShot). 'released' se déclenche quand le ballon part.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Dans la vue Code, le verbe est [`shoot`](/langage/verbes#shoot) : `shoot(power)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **4** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| puissance | `power` | nombre | `2000` | de 0 à 1000000 |
| hauteur | `lift` | nombre | `50` | de -5000 à 5000 |
| direction | `direction` | vecteur |  | optionnel |
| son | `sound` | texte | `vide` | écrit dans le bloc |
| particule | `particle` | texte | `vide` | écrit dans le bloc |
| particleTime | `particleTime` | nombre | `1.2` | de 0 à 10 |
| markStrength | `markStrength` | nombre | `0.95` | de 0 à 1 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| fired | `fired` | oui/non |  |  |
| released | `released` | flux |  |  |
| ball | `ball` | entité |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **puissance** (`power`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `2000`. Borné de 0 à 1000000.
- **hauteur** (`lift`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `50`. Borné de -5000 à 5000.
- **direction** (`direction`, vecteur). Le fil peut rester vide.
- **son** (`sound`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `vide`.
- **particule** (`particle`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `vide`.
- **particleTime** (`particleTime`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1.2`. Borné de 0 à 10.
- **markStrength** (`markStrength`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.95`. Borné de 0 à 1.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **fired** (`fired`, oui/non). Relie un fil bleu.
- **released** (`released`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **ball** (`ball`, entité). Relie un fil bleu.
