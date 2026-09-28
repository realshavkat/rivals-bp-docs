---
sidebar_position: 1
title: "Ball.Pulse"
sidebar_label: "Pulse"
description: "Onde visuelle existante du Skill Kit (BroadcastPulse)."
---

# Onde visuelle existante du Skill Kit (BroadcastPulse)

`Ball.Pulse`

Onde visuelle existante du Skill Kit (BroadcastPulse).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Ball.Pulse(pos = {0, 0, 0}, life = 0.35, radius = 48, r = 255)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| pos | `pos` | vecteur |  |  |
| life | `life` | nombre | `0.35` | de 0.05 à 5 |
| radius | `radius` | nombre | `48` | de 1 à 500 |
| r | `r` | entier | `255` | de 0 à 255 |
| g | `g` | entier | `255` | de 0 à 255 |
| b | `b` | entier | `255` | de 0 à 255 |
| a | `a` | entier | `160` | de 0 à 255 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **pos** (`pos`, vecteur). Relie un fil bleu.
- **life** (`life`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.35`. Borné de 0.05 à 5.
- **radius** (`radius`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `48`. Borné de 1 à 500.
- **r** (`r`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `255`. Borné de 0 à 255.
- **g** (`g`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `255`. Borné de 0 à 255.
- **b** (`b`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `255`. Borné de 0 à 255.
- **a** (`a`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `160`. Borné de 0 à 255.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
