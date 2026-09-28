---
sidebar_position: 9
title: "FX.SoundRandom"
sidebar_label: "SoundRandom"
description: "Joue un son choisi au hasard parmi 2 à 4 noms écrits en dur."
---

# Joue un son choisi au hasard parmi 2 à 4 noms écrits en dur

`FX.SoundRandom`

Joue un son choisi au hasard parmi 2 à 4 noms écrits en dur.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| name1 | `name1` | texte |  | écrit dans le bloc |
| name2 | `name2` | texte |  | écrit dans le bloc |
| name3 | `name3` | texte |  | optionnel, écrit dans le bloc |
| name4 | `name4` | texte |  | optionnel, écrit dans le bloc |
| cible | `entity` | entité |  | optionnel |
| niveau | `level` | nombre | `80` | de 20 à 180 |
| pitch | `pitch` | nombre | `100` | de 1 à 255 |
| volume | `volume` | nombre | `1` | de 0 à 1 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **name1** (`name1`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **name2** (`name2`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **name3** (`name3`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **name4** (`name4`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **cible** (`entity`, entité). Le fil peut rester vide.
- **niveau** (`level`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `80`. Borné de 20 à 180.
- **pitch** (`pitch`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `100`. Borné de 1 à 255.
- **volume** (`volume`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0 à 1.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
