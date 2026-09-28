---
sidebar_position: 2
title: "Action.Hit"
sidebar_label: "Hit"
description: "Fenêtre de frappe. Portée, dégâts, étourdissement, projection."
---

# Fenêtre de frappe

`Action.Hit`

Fenêtre de frappe. Portée, dégâts, étourdissement, projection.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Dans la vue Code, le verbe est [`hit`](/langage/verbes#hit) : `hit(range)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **4** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  | optionnel |
| cible | `mode` | texte | `player` | écrit dans le bloc, choix: `ball`, `player`, `any` |
| portée | `range` | nombre | `180` | de 16 à 2000 |
| angle | `cone` | nombre | `40` | de 5 à 180 |
| durée | `duration` | nombre | `0.35` | de 0.05 à 3 |
| dégâts | `damage` | nombre | `0` | de 0 à 100 |
| étourdir | `stun` | oui/non | `non` |  |
| stunTime | `stunTime` | nombre | `0.6` | de 0.05 à 5 |
| projection | `knock` | nombre | `0` | de 0 à 2000 |
| caméra | `shake` | oui/non | `oui` |  |
| force caméra | `amplitude` | nombre | `5` | de 0 à 20 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| touche | `hit` | flux |  |  |
| raté | `miss` | flux |  |  |
| cible | `target` | entité |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Tu peux laisser le fil vide: le bloc prend le lanceur.
- **cible** (`mode`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `player`. Valeurs prévues: `ball`, `player`, `any`.
- **portée** (`range`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `180`. Borné de 16 à 2000.
- **angle** (`cone`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `40`. Borné de 5 à 180.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.35`. Borné de 0.05 à 3.
- **dégâts** (`damage`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de 0 à 100.
- **étourdir** (`stun`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **stunTime** (`stunTime`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.6`. Borné de 0.05 à 5.
- **projection** (`knock`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de 0 à 2000.
- **caméra** (`shake`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **force caméra** (`amplitude`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `5`. Borné de 0 à 20.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **touche** (`hit`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **raté** (`miss`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **cible** (`target`, entité). Relie un fil bleu.
