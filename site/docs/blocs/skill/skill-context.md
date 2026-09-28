---
sidebar_position: 2
title: "Skill.Context"
sidebar_label: "Context"
description: "Lanceur et niveau de l'exécution courante."
---

# Lanceur et niveau de l'exécution courante

`Skill.Context`

Lanceur et niveau de l'exécution courante.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

Aucune.

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| lanceur | `caster` | joueur |  |  |
| niveau | `level` | entier |  |  |

## Détail

- **lanceur** (`caster`, joueur). Relie un fil bleu.
- **niveau** (`level`, entier). Relie un fil bleu.
