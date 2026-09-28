---
sidebar_position: 2
title: "Step.Projectile"
sidebar_label: "Projectile"
description: "Lance un projectile physique devant le lanceur, dans l'axe de sa visée (max 8 par exécution)."
---

# Projectile

`Step.Projectile`

Lance un projectile physique devant le lanceur, dans l'axe de sa visée (max 8 par exécution).

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Dans la vue Code, le verbe est [`projectile`](/langage/verbes#projectile) : `projectile(speed)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **10** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    projectile(1500, model = "models/props_junk/rock001a.mdl", lifetime = 3)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| model | `model` | texte | `models/props_junk/rock001a.mdl` | écrit dans le bloc |
| vitesse | `speed` | nombre | `1500` | de 0 à 5000 |
| lifetime | `lifetime` | nombre | `3` | de 0.1 à 10 |
| joueur | `player` | joueur |  | optionnel |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| cible | `entity` | entité |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **model** (`model`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `models/props_junk/rock001a.mdl`.
- **vitesse** (`speed`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1500`. Borné de 0 à 5000.
- **lifetime** (`lifetime`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `3`. Borné de 0.1 à 10.
- **joueur** (`player`, joueur). Le fil peut rester vide.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **cible** (`entity`, entité). Relie un fil bleu.
