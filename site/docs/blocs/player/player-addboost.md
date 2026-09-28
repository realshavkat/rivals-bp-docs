---
sidebar_position: 3
title: "Player.AddBoost"
sidebar_label: "AddBoost"
description: "AddBoost"
---

# AddBoost

`Player.AddBoost`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Player.AddBoost(player = caster, boost = "Shoot", percent = 0.02, duration = 60)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| boost | `boost` | texte |  | écrit dans le bloc, choix: `Shoot`, `Precision`, `Stamina`, `StaminaMax`, `Speed`, `Style`, `EXP` |
| percent | `percent` | nombre | `0.02` | de 0 à 1 |
| durée | `duration` | nombre | `60` | de 1 à 3600 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **boost** (`boost`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Valeurs prévues: `Shoot`, `Precision`, `Stamina`, `StaminaMax`, `Speed`, `Style`, `EXP`.
- **percent** (`percent`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.02`. Borné de 0 à 1.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `60`. Borné de 1 à 3600.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
