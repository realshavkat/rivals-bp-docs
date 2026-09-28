---
sidebar_position: 13
title: "Player.HurtFlash"
sidebar_label: "HurtFlash"
description: "Effet visuel « touché » existant chez le joueur ciblé (message Base::Hurted)."
---

# Effet visuel « touché » existant chez le joueur ciblé (message Base::Hurted)

`Player.HurtFlash`

Effet visuel « touché » existant chez le joueur ciblé (message Base::Hurted).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Player.HurtFlash(target = caster)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| cible | `target` | joueur |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **cible** (`target`, joueur). Relie un fil bleu.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
