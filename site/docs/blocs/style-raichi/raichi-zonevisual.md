---
sidebar_position: 2
title: "Raichi.ZoneVisual"
sidebar_label: "ZoneVisual"
description: "Effet visuel existant de la zone de Raichi (messages Raichi:Zone:Create / Remove)."
---

# ZoneVisual

`Raichi.ZoneVisual`

Effet visuel existant de la zone de Raichi (messages Raichi:Zone:Create / Remove).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Raichi.ZoneVisual(player = caster, enabled = true, duration = 8, radius = 128)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| enabled | `enabled` | oui/non | `oui` |  |
| durée | `duration` | nombre | `8` | de 0 à … |
| radius | `radius` | nombre | `128` | de 0 à 1500 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **enabled** (`enabled`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `8`. Borné de 0 à ….
- **radius** (`radius`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `128`. Borné de 0 à 1500.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
