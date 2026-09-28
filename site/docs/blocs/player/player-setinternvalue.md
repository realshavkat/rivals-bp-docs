---
sidebar_position: 18
title: "Player.SetInternValue"
sidebar_label: "SetInternValue"
description: "Valeur interne serveur du joueur (ex. verrou MaitriseParfaiteLock)."
---

# Valeur interne serveur du joueur (ex. verrou MaitriseParfaiteLock)

`Player.SetInternValue`

Valeur interne serveur du joueur (ex. verrou MaitriseParfaiteLock).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Player.SetInternValue(player = caster, key = "texte", value = 0)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| key | `key` | texte |  | écrit dans le bloc |
| valeur | `value` | nombre | `0` | de … à 1000000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **key** (`key`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **valeur** (`value`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de … à 1000000.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
