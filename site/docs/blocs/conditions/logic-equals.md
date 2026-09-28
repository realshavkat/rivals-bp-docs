---
sidebar_position: 2
title: "Logic.Equals"
sidebar_label: "Equals"
description: "Égalité stricte de deux valeurs quelconques (entités, chaînes...)."
---

# Égalité stricte de deux valeurs quelconques (entités, chaînes...)

`Logic.Equals`

Égalité stricte de deux valeurs quelconques (entités, chaînes...).

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| a | `a` | quelconque |  | optionnel |
| b | `b` | quelconque |  | optionnel |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | oui/non |  |  |

## Détail

- **a** (`a`, quelconque). Le fil peut rester vide.
- **b** (`b`, quelconque). Le fil peut rester vide.
- **résultat** (`result`, oui/non). Relie un fil bleu.
