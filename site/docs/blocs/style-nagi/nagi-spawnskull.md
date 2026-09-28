---
sidebar_position: 3
title: "Nagi.SpawnSkull"
sidebar_label: "SpawnSkull"
description: "Crâne de Nagi aux pieds du joueur (NAGI.SpawnSkull). skin auto = version Reo si la technique est copiée par Reo. Retiré à la fin de l'exécution."
---

# SpawnSkull

`Nagi.SpawnSkull`

Crâne de Nagi aux pieds du joueur (NAGI.SpawnSkull). skin auto = version Reo si la technique est copiée par Reo. Retiré à la fin de l'exécution.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Nagi.SpawnSkull(player = caster, skin = "auto")
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| skin | `skin` | texte | `auto` | écrit dans le bloc, choix: `auto`, `default`, `reo` |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **skin** (`skin`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `auto`. Valeurs prévues: `auto`, `default`, `reo`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
