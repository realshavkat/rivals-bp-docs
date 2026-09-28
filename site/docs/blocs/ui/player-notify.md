---
sidebar_position: 3
title: "Player.Notify"
sidebar_label: "Notify"
description: "Message au joueur."
---

# Afficher un texte

`Player.Notify`

Message au joueur.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`notify`](/langage/verbes#notify) : `notify(text)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| texte | `text` | texte |  | écrit dans le bloc |
| kind | `kind` | texte | `info` | écrit dans le bloc, choix: `info`, `rp`, `warning` |
| durée | `duration` | nombre | `3` | de 1 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **texte** (`text`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **kind** (`kind`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `info`. Valeurs prévues: `info`, `rp`, `warning`.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `3`. Borné de 1 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
