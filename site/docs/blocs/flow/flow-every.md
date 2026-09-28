---
sidebar_position: 7
title: "Flow.Every"
sidebar_label: "Every"
description: "Tâche périodique bornée (remplace les Think/timers par skill). 'stop' l'interrompt."
---

# Every

`Flow.Every`

Tâche périodique bornée (remplace les Think/timers par skill). 'stop' l'interrompt.

Enchaînement. Il décide quelle suite blanche part, et quand.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **2** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Flow.Every(interval = 0.1, count = 10)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| stop | `stop` | flux |  |  |
| interval | `interval` | nombre | `0.1` | de … à 10 |
| count | `count` | entier | `10` | de 1 à … |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| tick | `tick` | flux |  |  |
| index | `index` | entier |  |  |
| completed | `completed` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **stop** (`stop`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **interval** (`interval`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.1`. Borné de … à 10.
- **count** (`count`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `10`. Borné de 1 à ….
- **tick** (`tick`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **index** (`index`, entier). Relie un fil bleu.
- **completed** (`completed`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
