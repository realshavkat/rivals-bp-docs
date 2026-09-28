---
sidebar_position: 1
title: "Param.Get"
sidebar_label: "Get"
description: "Valeur d'un paramètre du graphe (résolu par niveau, compatible équilibrage)."
---

# Valeur d'un paramètre du graphe (résolu par niveau, compatible équilibrage)

`Param.Get`

Valeur d'un paramètre du graphe (résolu par niveau, compatible équilibrage).

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| nom | `name` | texte |  | écrit dans le bloc |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| valeur | `value` | quelconque |  |  |

## Détail

- **nom** (`name`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **valeur** (`value`, quelconque). Relie un fil bleu.
