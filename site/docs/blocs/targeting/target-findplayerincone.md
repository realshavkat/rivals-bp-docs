---
sidebar_position: 4
title: "Target.FindPlayerInCone"
sidebar_label: "FindPlayerInCone"
description: "Cible valide la plus proche dans le cône de visée (même dimension, règles du gamemode)."
---

# FindPlayerInCone

`Target.FindPlayerInCone`

Cible valide la plus proche dans le cône de visée (même dimension, règles du gamemode).

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Dans la vue Code, le verbe est [`find_target`](/langage/verbes#find_target) : `find_target(range, angle)`.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

Chaque passage consomme **6** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = find_target(300, 60, player = caster, requireSight = true)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |
| portée | `range` | nombre | `300` | de 16 à 3000 |
| angle | `angle` | nombre | `60` | de 1 à 180 |
| requireSight | `requireSight` | oui/non | `oui` |  |
| requireBall | `requireBall` | oui/non | `non` |  |
| anyPlayer | `anyPlayer` | oui/non | `non` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| cible | `target` | entité |  |  |
| found | `found` | oui/non |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **portée** (`range`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `300`. Borné de 16 à 3000.
- **angle** (`angle`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `60`. Borné de 1 à 180.
- **requireSight** (`requireSight`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **requireBall** (`requireBall`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **anyPlayer** (`anyPlayer`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **cible** (`target`, entité). Relie un fil bleu.
- **found** (`found`, oui/non). Relie un fil bleu.
