---
sidebar_position: 4
title: "Logic.Select"
sidebar_label: "Select"
description: "Retourne 'a' si condition, sinon 'b'."
---

# Retourne 'a' si condition, sinon 'b'

`Logic.Select`

Retourne 'a' si condition, sinon 'b'.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| condition | `condition` | oui/non |  |  |
| a | `a` | quelconque |  | optionnel |
| b | `b` | quelconque |  | optionnel |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| résultat | `result` | quelconque |  |  |

## Détail

- **condition** (`condition`, oui/non). Relie un fil bleu.
- **a** (`a`, quelconque). Le fil peut rester vide.
- **b** (`b`, quelconque). Le fil peut rester vide.
- **résultat** (`result`, quelconque). Relie un fil bleu.
