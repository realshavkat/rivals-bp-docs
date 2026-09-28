---
sidebar_position: 16
title: "Ball.Take"
sidebar_label: "Take"
description: "Le joueur prend un ballon libre (PLAYER:TakeBall)."
---

# Le joueur prend un ballon libre (PLAYER:TakeBall)

`Ball.Take`

Le joueur prend un ballon libre (PLAYER:TakeBall).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **2** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Ball.Take(player = caster, mode = "1")
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| ball | `ball` | entité |  |  |
| cible | `mode` | texte | `1` | écrit dans le bloc, choix: `1`, `torso` |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| taken | `taken` | oui/non |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **ball** (`ball`, entité). Relie un fil bleu.
- **cible** (`mode`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `1`. Valeurs prévues: `1`, `torso`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **taken** (`taken`, oui/non). Relie un fil bleu.
