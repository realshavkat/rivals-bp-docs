---
sidebar_position: 2
title: "FX.AttachModel"
sidebar_label: "AttachModel"
description: "Modèle client attaché au joueur (PLAYER:ParentModel existant)."
---

# Modèle client attaché au joueur (PLAYER:ParentModel existant)

`FX.AttachModel`

Modèle client attaché au joueur (PLAYER:ParentModel existant).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    FX.AttachModel(player = caster, model = "texte", bone = "Merge", duration = 1)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| model | `model` | texte |  | écrit dans le bloc |
| bone | `bone` | texte | `Merge` | écrit dans le bloc |
| durée | `duration` | nombre | `1` | de 0 à 3600 |
| scale | `scale` | nombre | `1` | de 0.05 à 10 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **model** (`model`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **bone** (`bone`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `Merge`.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0 à 3600.
- **scale** (`scale`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.05 à 10.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
