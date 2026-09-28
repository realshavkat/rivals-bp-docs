---
sidebar_position: 5
title: "FX.FlowEye"
sidebar_label: "FlowEye"
description: "Œil de Flow (PLAYER:FlowEye)."
---

# Œil de Flow (PLAYER:FlowEye)

`FX.FlowEye`

Œil de Flow (PLAYER:FlowEye).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    FX.FlowEye(player = caster, enabled = true, r = 255, g = 255)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| enabled | `enabled` | oui/non | `oui` |  |
| r | `r` | entier | `255` | de 0 à 255 |
| g | `g` | entier | `255` | de 0 à 255 |
| b | `b` | entier | `255` | de 0 à 255 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **enabled** (`enabled`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **r** (`r`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `255`. Borné de 0 à 255.
- **g** (`g`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `255`. Borné de 0 à 255.
- **b** (`b`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `255`. Borné de 0 à 255.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
