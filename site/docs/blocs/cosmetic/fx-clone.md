---
sidebar_position: 3
title: "FX.Clone"
sidebar_label: "Clone"
description: "Clone translucide du joueur (PLAYER:CreateClone, envoyé au PVS)."
---

# Clone translucide du joueur (PLAYER:CreateClone, envoyé au PVS)

`FX.Clone`

Clone translucide du joueur (PLAYER:CreateClone, envoyé au PVS).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    FX.Clone(player = caster, opacity = 0.9, duration = 3)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| opacity | `opacity` | nombre | `0.9` | de 0 à 1 |
| durée | `duration` | nombre | `3` | de 0.05 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **opacity** (`opacity`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.9`. Borné de 0 à 1.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `3`. Borné de 0.05 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
