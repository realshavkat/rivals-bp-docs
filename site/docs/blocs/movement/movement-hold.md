---
sidebar_position: 5
title: "Movement.Hold"
sidebar_label: "Hold"
description: "Immobilise le joueur (entrées à zéro, vitesse réduite à 'speed') pendant 'duration'. 'stop' libère tout de suite ; 'finished' à la fin normale."
---

# Hold

`Movement.Hold`

Immobilise le joueur (entrées à zéro, vitesse réduite à 'speed') pendant 'duration'. 'stop' libère tout de suite ; 'finished' à la fin normale.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Movement.Hold(player = caster, duration = 1, speed = 100)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| stop | `stop` | flux |  |  |
| joueur | `player` | joueur |  |  |
| durée | `duration` | nombre | `1` | de 0.02 à … |
| vitesse | `speed` | nombre | `100` | de 1 à 5000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| fini | `finished` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **stop** (`stop`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.02 à ….
- **vitesse** (`speed`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `100`. Borné de 1 à 5000.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **fini** (`finished`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
