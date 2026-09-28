---
sidebar_position: 1
title: "Zone.SlowAura"
sidebar_label: "SlowAura"
description: "Aura autour du lanceur : ralentit (sauf pendant un tir/lob) et draine la stamina des autres joueurs."
---

# SlowAura

`Zone.SlowAura`

Aura autour du lanceur : ralentit (sauf pendant un tir/lob) et draine la stamina des autres joueurs.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Dans la vue Code, le verbe est [`zone`](/langage/verbes#zone) : `zone(radius, duration)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **4** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| radius | `radius` | nombre | `128` | de 16 à 1500 |
| durée | `duration` | nombre | `8` | de 0.1 à … |
| slowPercent | `slowPercent` | nombre | `50` | de 0 à 95 |
| drain | `drain` | nombre | `0.5` | de 0 à 50 |
| staminaFloor | `staminaFloor` | nombre | `20` | de 0 à 1000 |
| interval | `interval` | nombre | `0.1` | de … à 1 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| fini | `finished` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **radius** (`radius`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `128`. Borné de 16 à 1500.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `8`. Borné de 0.1 à ….
- **slowPercent** (`slowPercent`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `50`. Borné de 0 à 95.
- **drain** (`drain`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.5`. Borné de 0 à 50.
- **staminaFloor** (`staminaFloor`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `20`. Borné de 0 à 1000.
- **interval** (`interval`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.1`. Borné de … à 1.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **fini** (`finished`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
