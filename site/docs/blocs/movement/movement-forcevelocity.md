---
sidebar_position: 4
title: "Movement.ForceVelocity"
sidebar_label: "ForceVelocity"
description: "Impose une vitesse au joueur pendant 'duration' secondes (prédit côté client)."
---

# Impose une vitesse au joueur pendant 'duration' secondes (prédit côté client)

`Movement.ForceVelocity`

Impose une vitesse au joueur pendant 'duration' secondes (prédit côté client).

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Movement.ForceVelocity(player = caster, direction = {0, 0, 0}, speed = 1000, duration = 0.3)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| direction | `direction` | vecteur |  |  |
| vitesse | `speed` | nombre | `1000` | de 0 à 4000 |
| durée | `duration` | nombre | `0.3` | de 0.05 à 5 |
| keepVertical | `keepVertical` | oui/non | `oui` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| fini | `finished` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **direction** (`direction`, vecteur). Relie un fil bleu.
- **vitesse** (`speed`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1000`. Borné de 0 à 4000.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.3`. Borné de 0.05 à 5.
- **keepVertical** (`keepVertical`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **fini** (`finished`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
