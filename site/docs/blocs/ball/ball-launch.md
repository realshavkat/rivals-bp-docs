---
sidebar_position: 6
title: "Ball.Launch"
sidebar_label: "Launch"
description: "Le joueur lâche son ballon et le frappe : direction × force + lift vertical."
---

# Le joueur lâche son ballon et le frappe : direction × force + lift vertical

`Ball.Launch`

Le joueur lâche son ballon et le frappe : direction × force + lift vertical.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`launch`](/langage/verbes#launch) : `launch(force)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **4** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| direction | `direction` | vecteur |  | optionnel |
| force | `force` | nombre | `2000` | de 0 à 8000 |
| hauteur | `lift` | nombre | `50` | de -2000 à 2000 |
| powerShot | `powerShot` | oui/non | `non` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| launched | `launched` | oui/non |  |  |
| ball | `ball` | entité |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **direction** (`direction`, vecteur). Le fil peut rester vide.
- **force** (`force`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `2000`. Borné de 0 à 8000.
- **hauteur** (`lift`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `50`. Borné de -2000 à 2000.
- **powerShot** (`powerShot`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **launched** (`launched`, oui/non). Relie un fil bleu.
- **ball** (`ball`, entité). Relie un fil bleu.
