---
sidebar_position: 9
title: "Player.GetBoost"
sidebar_label: "GetBoost"
description: "Boost actif du joueur (PLAYER:GetBoost) : active, value (fraction, ex. 0.03 = 3 %)."
---

# GetBoost

`Player.GetBoost`

Boost actif du joueur (PLAYER:GetBoost) : active, value (fraction, ex. 0.03 = 3 %).

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |
| boost | `boost` | texte |  | écrit dans le bloc, choix: `Shoot`, `Precision`, `Stamina`, `StaminaMax`, `Speed`, `Style`, `EXP` |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| active | `active` | oui/non |  |  |
| valeur | `value` | nombre |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **boost** (`boost`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Valeurs prévues: `Shoot`, `Precision`, `Stamina`, `StaminaMax`, `Speed`, `Style`, `EXP`.
- **active** (`active`, oui/non). Relie un fil bleu.
- **valeur** (`value`, nombre). Relie un fil bleu.
