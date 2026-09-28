---
sidebar_position: 1
title: "Otoya.SetHidden"
sidebar_label: "SetHidden"
description: "Invisibilité du mode Ninja d'Otoya (hidden = true) ou fin de l'invisibilité. Toujours retirée à la fin de l'exécution."
---

# SetHidden

`Otoya.SetHidden`

Invisibilité du mode Ninja d'Otoya (hidden = true) ou fin de l'invisibilité. Toujours retirée à la fin de l'exécution.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Otoya.SetHidden(player = caster, hidden = true, duration = 6)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| hidden | `hidden` | oui/non | `oui` |  |
| durée | `duration` | nombre | `6` | de 0.05 à … |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **hidden** (`hidden`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `6`. Borné de 0.05 à ….
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
