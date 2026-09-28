---
sidebar_position: 1
title: "Nagi.ReleasePowerShot"
sidebar_label: "ReleasePowerShot"
description: "Lâche le ballon à sa position exacte puis le tire façon Nagi (vitesse de pointe maintenue sur burstDistance). Sans la bibliothèque, tir droit dans l'axe de visée."
---

# ReleasePowerShot

`Nagi.ReleasePowerShot`

Lâche le ballon à sa position exacte puis le tire façon Nagi (vitesse de pointe maintenue sur burstDistance). Sans la bibliothèque, tir droit dans l'axe de visée.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **5** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| ball | `ball` | entité |  |  |
| peakSpeed | `peakSpeed` | nombre | `3200` | de 0 à 10000 |
| burstDistance | `burstDistance` | nombre | `950` | de 0 à 5000 |
| cible | `mode` | texte | `burst` | écrit dans le bloc, choix: `burst`, `straight` |
| exactPos | `exactPos` | oui/non | `oui` |  |
| auraTime | `auraTime` | nombre | `1.35` | de 0 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **ball** (`ball`, entité). Relie un fil bleu.
- **peakSpeed** (`peakSpeed`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `3200`. Borné de 0 à 10000.
- **burstDistance** (`burstDistance`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `950`. Borné de 0 à 5000.
- **cible** (`mode`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `burst`. Valeurs prévues: `burst`, `straight`.
- **exactPos** (`exactPos`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **auraTime** (`auraTime`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1.35`. Borné de 0 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
