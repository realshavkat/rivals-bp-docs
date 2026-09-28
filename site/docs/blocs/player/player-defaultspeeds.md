---
sidebar_position: 8
title: "Player.DefaultSpeeds"
sidebar_label: "DefaultSpeeds"
description: "Vitesses de marche et de course par défaut du joueur (personnage, stats)."
---

# Vitesses de marche et de course par défaut du joueur (personnage, stats)

`Player.DefaultSpeeds`

Vitesses de marche et de course par défaut du joueur (personnage, stats).

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Player.DefaultSpeeds(player = caster)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| walk | `walk` | nombre |  |  |
| run | `run` | nombre |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **walk** (`walk`, nombre). Relie un fil bleu.
- **run** (`run`, nombre). Relie un fil bleu.
