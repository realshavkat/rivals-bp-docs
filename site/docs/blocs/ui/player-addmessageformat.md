---
sidebar_position: 2
title: "Player.AddMessageFormat"
sidebar_label: "AddMessageFormat"
description: "Message du HUD (PLAYER:AddMessage) dont le texte contient {1} à {5}, remplacés par les valeurs reliées."
---

# AddMessageFormat

`Player.AddMessageFormat`

Message du HUD (PLAYER:AddMessage) dont le texte contient &#123;1&#125; à &#123;5&#125;, remplacés par les valeurs reliées.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| texte | `text` | texte |  | écrit dans le bloc |
| v1 | `v1` | quelconque |  | optionnel |
| v2 | `v2` | quelconque |  | optionnel |
| v3 | `v3` | quelconque |  | optionnel |
| v4 | `v4` | quelconque |  | optionnel |
| v5 | `v5` | quelconque |  | optionnel |
| durée | `duration` | nombre | `3` | de 0.5 à 10 |
| code | `code` | entier | `1` | de 0 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **texte** (`text`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **v1** (`v1`, quelconque). Le fil peut rester vide.
- **v2** (`v2`, quelconque). Le fil peut rester vide.
- **v3** (`v3`, quelconque). Le fil peut rester vide.
- **v4** (`v4`, quelconque). Le fil peut rester vide.
- **v5** (`v5`, quelconque). Le fil peut rester vide.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `3`. Borné de 0.5 à 10.
- **code** (`code`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
