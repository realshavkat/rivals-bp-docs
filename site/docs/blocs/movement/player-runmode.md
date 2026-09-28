---
sidebar_position: 14
title: "Player.RunMode"
sidebar_label: "RunMode"
description: "Active/désactive le mode course du gamemode (RunModeKuro)."
---

# Active/désactive le mode course du gamemode (RunModeKuro)

`Player.RunMode`

Active/désactive le mode course du gamemode (RunModeKuro).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Player.RunMode(player = caster, enabled = false, speed = 500)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| enabled | `enabled` | oui/non | `non` |  |
| vitesse | `speed` | nombre | `500` | de 1 à 3000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **enabled** (`enabled`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **vitesse** (`speed`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `500`. Borné de 1 à 3000.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
