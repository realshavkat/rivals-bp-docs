---
sidebar_position: 3
title: "Balance.Number"
sidebar_label: "Number"
description: "Valeur numérique d'équilibrage (force, durée, multiplicateur)."
---

# Valeur numérique d'équilibrage (force, durée, multiplicateur)

`Balance.Number`

Valeur numérique d'équilibrage (force, durée, multiplicateur).

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Balance.Number(value = 1, label = "valeur")
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| valeur | `value` | nombre | `1` | de -1000000 à 1000000 |
| label | `label` | texte | `valeur` | écrit dans le bloc |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| valeur | `value` | nombre |  |  |

## Détail

- **valeur** (`value`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de -1000000 à 1000000.
- **label** (`label`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `valeur`.
- **valeur** (`value`, nombre). Relie un fil bleu.
