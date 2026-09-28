---
sidebar_position: 4
title: "Player.NotifySkillName"
sidebar_label: "NotifySkillName"
description: "Notification dont le texte contient {nom}, remplacé par le nom de la technique 'skillId'."
---

# NotifySkillName

`Player.NotifySkillName`

Notification dont le texte contient &#123;nom&#125;, remplacé par le nom de la technique 'skillId'.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| texte | `text` | texte |  | écrit dans le bloc |
| skillId | `skillId` | texte |  |  |
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
- **skillId** (`skillId`, texte). Relie un fil bleu.
- **kind** (`kind`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `info`. Valeurs prévues: `info`, `rp`, `warning`.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `3`. Borné de 1 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
