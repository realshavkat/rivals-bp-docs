---
sidebar_position: 11
title: "Target.IsValidTarget"
sidebar_label: "IsValidTarget"
description: "Revalidation serveur d'une cible : règles du gamemode, distance max, ligne de vue."
---

# IsValidTarget

`Target.IsValidTarget`

Revalidation serveur d'une cible : règles du gamemode, distance max, ligne de vue.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

Chaque passage consomme **5** dans le budget d'exécution (le défaut est 1).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |
| cible | `target` | entité |  |  |
| maxRange | `maxRange` | nombre | `500` | de 1 à 5000 |
| requireSight | `requireSight` | oui/non | `oui` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| valid | `valid` | oui/non |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **cible** (`target`, entité). Relie un fil bleu.
- **maxRange** (`maxRange`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `500`. Borné de 1 à 5000.
- **requireSight** (`requireSight`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **valid** (`valid`, oui/non). Relie un fil bleu.
