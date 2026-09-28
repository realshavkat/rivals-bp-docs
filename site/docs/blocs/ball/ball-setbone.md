---
sidebar_position: 9
title: "Ball.SetBone"
sidebar_label: "SetBone"
description: "Attache visuelle du ballon sur un os ('' = normal, ex. ball_fx3, cc_ball)."
---

# Attache visuelle du ballon sur un os ('' = normal, ex. ball_fx3, cc_ball)

`Ball.SetBone`

Attache visuelle du ballon sur un os ('' = normal, ex. ball_fx3, cc_ball).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Ball.SetBone()
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| ball | `ball` | entité |  |  |
| bone | `bone` | texte | `vide` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **ball** (`ball`, entité). Relie un fil bleu.
- **bone** (`bone`, texte). Sans fil bleu, le défaut est utilisé. Défaut: `vide`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
