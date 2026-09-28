---
sidebar_position: 13
title: "Ball.SetVelocity"
sidebar_label: "SetVelocity"
description: "set = SetVelocity, instant = SetVelocityInstantaneous, add = AddVelocity, launch = BL.SoccerBall.LaunchBall (bornes minZ/maxZ)."
---

# SetVelocity

`Ball.SetVelocity`

set = SetVelocity, instant = SetVelocityInstantaneous, add = AddVelocity, launch = BL.SoccerBall.LaunchBall (bornes minZ/maxZ).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **2** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| ball | `ball` | entité |  |  |
| velocity | `velocity` | vecteur |  |  |
| cible | `mode` | texte | `set` | écrit dans le bloc, choix: `set`, `instant`, `add`, `launch` |
| minZ | `minZ` | nombre |  | optionnel, de … à 1000000 |
| maxZ | `maxZ` | nombre |  | optionnel, de … à 1000000 |
| resetSpin | `resetSpin` | oui/non | `non` |  |
| powerShot | `powerShot` | oui/non | `non` |  |
| markStrength | `markStrength` | nombre | `0.95` | de 0 à 1 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **ball** (`ball`, entité). Relie un fil bleu.
- **velocity** (`velocity`, vecteur). Relie un fil bleu.
- **cible** (`mode`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `set`. Valeurs prévues: `set`, `instant`, `add`, `launch`.
- **minZ** (`minZ`, nombre). Le fil peut rester vide. Borné de … à 1000000.
- **maxZ** (`maxZ`, nombre). Le fil peut rester vide. Borné de … à 1000000.
- **resetSpin** (`resetSpin`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **powerShot** (`powerShot`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **markStrength** (`markStrength`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.95`. Borné de 0 à 1.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
