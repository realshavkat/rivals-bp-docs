---
sidebar_position: 12
title: "Player.Freeze"
sidebar_label: "Freeze"
description: "Fige un joueur (lanceur ou cible) pendant 'duration', libéré même si l'exécution est annulée."
---

# Freeze

`Player.Freeze`

Fige un joueur (lanceur ou cible) pendant 'duration', libéré même si l'exécution est annulée.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Dans la vue Code, le verbe est [`freeze`](/langage/verbes#freeze) : `freeze(duration)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    freeze(1, player = caster, moveTypeNone = false)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| durée | `duration` | nombre | `1` | de 0.02 à 10 |
| moveTypeNone | `moveTypeNone` | oui/non | `non` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.02 à 10.
- **moveTypeNone** (`moveTypeNone`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
