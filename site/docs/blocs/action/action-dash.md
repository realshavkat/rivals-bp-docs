---
sidebar_position: 1
title: "Action.Dash"
sidebar_label: "Dash"
description: "Dash avec effet. Direction, vitesse, son et particule."
---

# Dash avec effet

`Action.Dash`

Dash avec effet. Direction, vitesse, son et particule.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`dash`](/langage/verbes#dash) : `dash(direction)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **3** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    dash("forward", speed = 900, duration = 0.28)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  | optionnel |
| direction | `direction` | texte | `forward` | choix: `forward`, `back`, `left`, `right` |
| vitesse | `speed` | nombre | `900` | de 0 à 3000 |
| durée | `duration` | nombre | `0.28` | de 0.05 à 3 |
| particule | `particle` | texte | `vide` | optionnel, écrit dans le bloc |
| son | `sound` | texte | `vide` | optionnel, écrit dans le bloc |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Tu peux laisser le fil vide: le bloc prend le lanceur.
- **direction** (`direction`, texte). Sans fil bleu, le défaut est utilisé. Défaut: `forward`. Valeurs prévues: `forward`, `back`, `left`, `right`.
- **vitesse** (`speed`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `900`. Borné de 0 à 3000.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.28`. Borné de 0.05 à 3.
- **particule** (`particle`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `vide`.
- **son** (`sound`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `vide`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
