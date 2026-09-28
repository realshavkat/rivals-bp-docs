---
sidebar_position: 5
title: "Player.AimDirection"
sidebar_label: "AimDirection"
description: "Direction de visée du joueur (flat = sans composante verticale)."
---

# Direction de visée du joueur (flat = sans composante verticale)

`Player.AimDirection`

Direction de visée du joueur (flat = sans composante verticale).

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Dans la vue Code, le verbe est [`aim`](/langage/verbes#aim).

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = aim(player = caster, flat = false)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| joueur | `player` | joueur |  |  |
| flat | `flat` | oui/non | `non` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| direction | `direction` | vecteur |  |  |
| eyePos | `eyePos` | vecteur |  |  |
| angles | `angles` | angle |  |  |

## Détail

- **joueur** (`player`, joueur). Relie un fil bleu.
- **flat** (`flat`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **direction** (`direction`, vecteur). Relie un fil bleu.
- **eyePos** (`eyePos`, vecteur). Relie un fil bleu.
- **angles** (`angles`, angle). Relie un fil bleu.
