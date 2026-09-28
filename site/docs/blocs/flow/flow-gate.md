---
sidebar_position: 10
title: "Flow.Gate"
sidebar_label: "Gate"
description: "Gate"
---

# Gate

`Flow.Gate`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Enchaînement. Il décide quelle suite blanche part, et quand.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Flow.Gate(startClosed = false)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| enter | `enter` | flux |  |  |
| open | `open` | flux |  |  |
| close | `close` | flux |  |  |
| toggle | `toggle` | flux |  |  |
| startClosed | `startClosed` | oui/non | `non` | écrit dans le bloc |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| exit | `exit` | flux |  |  |

## Détail

- **enter** (`enter`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **open** (`open`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **close** (`close`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **toggle** (`toggle`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **startClosed** (`startClosed`, oui/non). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `non`.
- **exit** (`exit`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
