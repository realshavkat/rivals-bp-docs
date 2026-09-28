---
sidebar_position: 9
title: "Player.KeyDown"
sidebar_label: "KeyDown"
description: "KeyDown"
---

# KeyDown

`Player.KeyDown`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Player.KeyDown(player = caster, key = "texte")
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |
| key | `key` | texte |  | écrit dans le bloc |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| down | `down` | oui/non |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **key** (`key`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **down** (`down`, oui/non). Relie un fil bleu.
