---
sidebar_position: 15
title: "Player.SetHeadPreset"
sidebar_label: "SetHeadPreset"
description: "Tête temporaire du personnage (PLAYER:SetHeadPresetTemporary) ; 'old' = tête d'origine à restaurer (0 si inchangée). 0 ou moins = tête 1."
---

# SetHeadPreset

`Player.SetHeadPreset`

Tête temporaire du personnage (PLAYER:SetHeadPresetTemporary) ; 'old' = tête d'origine à restaurer (0 si inchangée). 0 ou moins = tête 1.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Player.SetHeadPreset(player = caster, preset = 1)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| preset | `preset` | entier | `1` | de 0 à 64 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| old | `old` | entier |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **preset** (`preset`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0 à 64.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **old** (`old`, entier). Relie un fil bleu.
