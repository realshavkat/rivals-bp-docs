---
sidebar_position: 7
title: "Player.IsInStyle"
sidebar_label: "IsInStyle"
description: "Vrai si le style de jeu OU la classe du joueur correspond."
---

# Vrai si le style de jeu OU la classe du joueur correspond

`Player.IsInStyle`

Vrai si le style de jeu OU la classe du joueur correspond.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |
| style | `style` | texte |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | oui/non |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **style** (`style`, texte). Relie un fil bleu.
- **résultat** (`result`, oui/non). Relie un fil bleu.
