---
sidebar_position: 15
title: "Ball.StraightPass"
sidebar_label: "StraightPass"
description: "Passe directe au sol vers un coéquipier (non guidée) : vitesse fixe, temps de retouche calculé."
---

# StraightPass

`Ball.StraightPass`

Passe directe au sol vers un coéquipier (non guidée) : vitesse fixe, temps de retouche calculé.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`pass`](/langage/verbes#pass) : `pass(target)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **4** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| cible | `target` | entité |  |  |
| vitesse | `speed` | nombre | `900` | de 450 à 5000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| passed | `passed` | oui/non |  |  |
| ball | `ball` | entité |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **cible** (`target`, entité). Relie un fil bleu.
- **vitesse** (`speed`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `900`. Borné de 450 à 5000.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **passed** (`passed`, oui/non). Relie un fil bleu.
- **ball** (`ball`, entité). Relie un fil bleu.
