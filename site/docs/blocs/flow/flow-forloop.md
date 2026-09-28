---
sidebar_position: 9
title: "Flow.ForLoop"
sidebar_label: "ForLoop"
description: "Boucle bornée (max 64 itérations)."
---

# Boucle bornée (max 64 itérations)

`Flow.ForLoop`

Boucle bornée (max 64 itérations).

Enchaînement. Il décide quelle suite blanche part, et quand.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **2** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Flow.ForLoop(first = 1, last = 1)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| first | `first` | entier | `1` | de -1000 à 1000 |
| last | `last` | entier | `1` | de -1000 à 1000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| body | `body` | flux |  |  |
| index | `index` | entier |  |  |
| completed | `completed` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **first** (`first`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de -1000 à 1000.
- **last** (`last`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de -1000 à 1000.
- **body** (`body`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **index** (`index`, entier). Relie un fil bleu.
- **completed** (`completed`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
