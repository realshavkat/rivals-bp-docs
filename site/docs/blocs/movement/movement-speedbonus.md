---
sidebar_position: 7
title: "Movement.SpeedBonus"
sidebar_label: "SpeedBonus"
description: "Ajoute 'run' à la vitesse de course et 'walk' à la marche actuelles pendant 'duration' (ou jusqu'à 'stop')."
---

# SpeedBonus

`Movement.SpeedBonus`

Ajoute 'run' à la vitesse de course et 'walk' à la marche actuelles pendant 'duration' (ou jusqu'à 'stop').

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Movement.SpeedBonus(player = caster, run = 25, walk = 16, duration = 6)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| stop | `stop` | flux |  |  |
| joueur | `player` | joueur |  |  |
| run | `run` | nombre | `25` | de -2000 à 2000 |
| walk | `walk` | nombre | `16` | de -2000 à 2000 |
| durée | `duration` | nombre | `6` | de 0.02 à … |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **stop** (`stop`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **run** (`run`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `25`. Borné de -2000 à 2000.
- **walk** (`walk`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `16`. Borné de -2000 à 2000.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `6`. Borné de 0.02 à ….
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
