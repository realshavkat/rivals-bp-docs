---
sidebar_position: 1
title: "Balance.Bool"
sidebar_label: "Bool"
description: "Interrupteur d'équilibrage."
---

# Interrupteur d'équilibrage

`Balance.Bool`

Interrupteur d'équilibrage.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Balance.Bool(enabled = true, label = "flag")
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| enabled | `enabled` | oui/non | `oui` |  |
| label | `label` | texte | `flag` | écrit dans le bloc |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| enabled | `enabled` | oui/non |  |  |

## Détail

- **enabled** (`enabled`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **label** (`label`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `flag`.
- **enabled** (`enabled`, oui/non). Relie un fil bleu.
