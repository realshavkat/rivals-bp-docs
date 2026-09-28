---
sidebar_position: 4
title: "Balance.Percent"
sidebar_label: "Percent"
description: "Pourcentage 0-100 converti en facteur 0-1."
---

# Pourcentage 0-100 converti en facteur 0-1

`Balance.Percent`

Pourcentage 0-100 converti en facteur 0-1.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| percent | `percent` | nombre | `100` | de 0 à 100 |
| label | `label` | texte | `chance` | écrit dans le bloc |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| factor | `factor` | nombre |  |  |
| percent | `percent` | nombre |  |  |

## Détail

- **percent** (`percent`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `100`. Borné de 0 à 100.
- **label** (`label`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `chance`.
- **factor** (`factor`, nombre). Relie un fil bleu.
- **percent** (`percent`, nombre). Relie un fil bleu.
