---
sidebar_position: 18
title: "Player.SetPos"
sidebar_label: "SetPos"
description: "Téléporte le joueur ; refusé si la destination est à plus de 'maxDistance' (anti-abus)."
---

# SetPos

`Player.SetPos`

Téléporte le joueur ; refusé si la destination est à plus de 'maxDistance' (anti-abus).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`teleport`](/langage/verbes#teleport) : `teleport(pos)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    teleport({0, 0, 0}, player = caster, maxDistance = 500)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| pos | `pos` | vecteur |  |  |
| maxDistance | `maxDistance` | nombre | `500` | de 1 à 3000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| moved | `moved` | oui/non |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **pos** (`pos`, vecteur). Relie un fil bleu.
- **maxDistance** (`maxDistance`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `500`. Borné de 1 à 3000.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **moved** (`moved`, oui/non). Relie un fil bleu.
