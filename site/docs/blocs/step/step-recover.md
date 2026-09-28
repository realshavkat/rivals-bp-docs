---
sidebar_position: 3
title: "Step.Recover"
sidebar_label: "Recover"
description: "Récupération : le lanceur est ralenti (multiplicateur) pendant 'seconds', puis la suite."
---

# Recover

`Step.Recover`

Récupération : le lanceur est ralenti (multiplicateur) pendant 'seconds', puis la suite.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Dans la vue Code, le verbe est [`recover`](/langage/verbes#recover) : `recover(seconds)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    recover(0.3, slow = 0.6)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| secondes | `seconds` | nombre | `0.3` | de 0 à 5 |
| slow | `slow` | nombre | `0.6` | de … à 1 |
| joueur | `player` | joueur |  | optionnel |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **secondes** (`seconds`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.3`. Borné de 0 à 5.
- **slow** (`slow`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.6`. Borné de … à 1.
- **joueur** (`player`, joueur). Le fil peut rester vide.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
