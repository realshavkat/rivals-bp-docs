---
sidebar_position: 11
title: "Ball.SetPos"
sidebar_label: "SetPos"
description: "SetPos"
---

# SetPos

`Ball.SetPos`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Ball.SetPos(pos = {0, 0, 0})
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| ball | `ball` | entité |  |  |
| pos | `pos` | vecteur |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **ball** (`ball`, entité). Relie un fil bleu.
- **pos** (`pos`, vecteur). Relie un fil bleu.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
