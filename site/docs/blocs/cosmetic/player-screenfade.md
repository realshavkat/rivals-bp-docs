---
sidebar_position: 15
title: "Player.ScreenFade"
sidebar_label: "ScreenFade"
description: "ScreenFade"
---

# ScreenFade

`Player.ScreenFade`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Player.ScreenFade(player = caster, r = 255, g = 255, b = 255)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| r | `r` | entier | `255` | de 0 à 255 |
| g | `g` | entier | `255` | de 0 à 255 |
| b | `b` | entier | `255` | de 0 à 255 |
| a | `a` | entier | `128` | de 0 à 255 |
| durée | `duration` | nombre | `0.3` | de 0 à 5 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **r** (`r`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `255`. Borné de 0 à 255.
- **g** (`g`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `255`. Borné de 0 à 255.
- **b** (`b`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `255`. Borné de 0 à 255.
- **a** (`a`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `128`. Borné de 0 à 255.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.3`. Borné de 0 à 5.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
