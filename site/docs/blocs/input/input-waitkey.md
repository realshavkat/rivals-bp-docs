---
sidebar_position: 1
title: "Input.WaitKey"
sidebar_label: "WaitKey"
description: "Attend qu'une touche soit pressée par le lanceur (détection serveur, aucun message client)."
---

# WaitKey

`Input.WaitKey`

Attend qu'une touche soit pressée par le lanceur (détection serveur, aucun message client).

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| key | `key` | texte |  | écrit dans le bloc, choix: `attack`, `attack2`, `jump`, `duck`, `use`, `reload`, `forward`, `back`, `moveleft`, `moveright`, `speed`, `walk` |
| key2 | `key2` | texte |  | optionnel, écrit dans le bloc, choix: `attack`, `attack2`, `jump`, `duck`, `use`, `reload`, `forward`, `back`, `moveleft`, `moveright`, `speed`, `walk` |
| timeout | `timeout` | nombre | `1` | de 0.05 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| pressed | `pressed` | flux |  |  |
| pressedKey | `pressedKey` | texte |  |  |
| timeout | `timeout` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **key** (`key`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Valeurs prévues: `attack`, `attack2`, `jump`, `duck`, `use`, `reload`, `forward`, `back`, `moveleft`, `moveright`, `speed`, `walk`.
- **key2** (`key2`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Valeurs prévues: `attack`, `attack2`, `jump`, `duck`, `use`, `reload`, `forward`, `back`, `moveleft`, `moveright`, `speed`, `walk`.
- **timeout** (`timeout`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.05 à 10.
- **pressed** (`pressed`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **pressedKey** (`pressedKey`, texte). Relie un fil bleu.
- **timeout** (`timeout`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
