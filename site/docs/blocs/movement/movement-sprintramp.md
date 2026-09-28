---
sidebar_position: 10
title: "Movement.SprintRamp"
sidebar_label: "SprintRamp"
description: "Pendant 'duration' : tant que Maj est tenu, la vitesse de course monte de 'from' à 'to' (mode course du gamemode). lockSide empêche les pas de côté (prédit). 'stop' arrête l'effet ; 'finished' part à la fin de la durée dans tous les cas."
---

# SprintRamp

`Movement.SprintRamp`

Pendant 'duration' : tant que Maj est tenu, la vitesse de course monte de 'from' à 'to' (mode course du gamemode). lockSide empêche les pas de côté (prédit). 'stop' arrête l'effet ; 'finished' part à la fin de la durée dans tous les cas.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Movement.SprintRamp(player = caster, from = 400, to = 700, duration = 3)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| stop | `stop` | flux |  |  |
| joueur | `player` | joueur |  |  |
| from | `from` | nombre | `400` | de 1 à 3000 |
| to | `to` | nombre | `700` | de 1 à 3000 |
| durée | `duration` | nombre | `3` | de 0.05 à … |
| lockSide | `lockSide` | oui/non | `non` |  |
| runMode | `runMode` | oui/non | `oui` |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| fini | `finished` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **stop** (`stop`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **from** (`from`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `400`. Borné de 1 à 3000.
- **to** (`to`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `700`. Borné de 1 à 3000.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `3`. Borné de 0.05 à ….
- **lockSide** (`lockSide`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **runMode** (`runMode`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **fini** (`finished`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
