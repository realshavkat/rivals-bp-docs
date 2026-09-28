---
sidebar_position: 12
title: "Player.ClientSignal"
sidebar_label: "ClientSignal"
description: "Déclenche l'effet client existant d'une technique (liste fermée), avec une valeur numérique."
---

# ClientSignal

`Player.ClientSignal`

Déclenche l'effet client existant d'une technique (liste fermée), avec une valeur numérique.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Player.ClientSignal(player = caster, signal = "WildcardCardRotation", value = 0)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| signal | `signal` | texte |  | écrit dans le bloc, choix: `WildcardCardRotation` |
| valeur | `value` | nombre | `0` | de -100000 à 100000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **signal** (`signal`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Valeurs prévues: `WildcardCardRotation`.
- **valeur** (`value`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de -100000 à 100000.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
