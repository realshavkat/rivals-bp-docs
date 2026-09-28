---
sidebar_position: 5
title: "Anim.TrickAnim"
sidebar_label: "TrickAnim"
description: "Séquence de geste technique fournie par le système de mouvement (hook BL::RivalsMove::TrickAnim), sinon 'fallback'."
---

# TrickAnim

`Anim.TrickAnim`

Séquence de geste technique fournie par le système de mouvement (hook BL::RivalsMove::TrickAnim), sinon 'fallback'.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |
| trick | `trick` | texte |  | écrit dans le bloc |
| side | `side` | texte |  | écrit dans le bloc |
| fallback | `fallback` | texte |  | écrit dans le bloc |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| animation | `sequence` | texte |  |  |
| isTrick | `isTrick` | oui/non |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **trick** (`trick`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **side** (`side`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **fallback** (`fallback`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **animation** (`sequence`, texte). Relie un fil bleu.
- **isTrick** (`isTrick`, oui/non). Relie un fil bleu.
