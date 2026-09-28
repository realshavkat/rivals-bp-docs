---
sidebar_position: 20
title: "Player.SetNetFlag"
sidebar_label: "SetNetFlag"
description: "Drapeau NetVar du gamemode lu par d'autres systèmes (OtoyaNinjaMode : tacle garanti). Remis à false à la fin de l'exécution."
---

# SetNetFlag

`Player.SetNetFlag`

Drapeau NetVar du gamemode lu par d'autres systèmes (OtoyaNinjaMode : tacle garanti). Remis à false à la fin de l'exécution.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| flag | `flag` | texte |  | écrit dans le bloc, choix: `OtoyaNinjaMode` |
| valeur | `value` | oui/non | `oui` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **flag** (`flag`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Valeurs prévues: `OtoyaNinjaMode`.
- **valeur** (`value`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
