---
sidebar_position: 3
title: "Player.Axes"
sidebar_label: "Axes"
description: "Axes de la vue du joueur (flat = sans tangage) et direction du corps."
---

# Axes de la vue du joueur (flat = sans tangage) et direction du corps

`Player.Axes`

Axes de la vue du joueur (flat = sans tangage) et direction du corps.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |
| flat | `flat` | oui/non | `oui` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| forward | `forward` | vecteur |  |  |
| right | `right` | vecteur |  |  |
| up | `up` | vecteur |  |  |
| bodyForward | `bodyForward` | vecteur |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **flat** (`flat`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **forward** (`forward`, vecteur). Relie un fil bleu.
- **right** (`right`, vecteur). Relie un fil bleu.
- **up** (`up`, vecteur). Relie un fil bleu.
- **bodyForward** (`bodyForward`, vecteur). Relie un fil bleu.
