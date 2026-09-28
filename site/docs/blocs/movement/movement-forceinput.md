---
sidebar_position: 3
title: "Movement.ForceInput"
sidebar_label: "ForceInput"
description: "Simule les touches de déplacement (avance/côté/sprint) pendant 'duration'. Prédit côté client."
---

# ForceInput

`Movement.ForceInput`

Simule les touches de déplacement (avance/côté/sprint) pendant 'duration'. Prédit côté client.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| forward | `forward` | nombre | `1000` | de … à 1000000 |
| side | `side` | nombre | `0` | de … à 1000000 |
| sprint | `sprint` | oui/non | `oui` |  |
| durée | `duration` | nombre | `0.5` | de 0.02 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **forward** (`forward`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1000`. Borné de … à 1000000.
- **side** (`side`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de … à 1000000.
- **sprint** (`sprint`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.5`. Borné de 0.02 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
