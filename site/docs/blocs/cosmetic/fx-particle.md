---
sidebar_position: 6
title: "FX.Particle"
sidebar_label: "Particle"
description: "Particule sur une entité (follow/point) ou à une position (none)."
---

# Particule

`FX.Particle`

Particule sur une entité (follow/point) ou à une position (none).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`particle`](/langage/verbes#particle) : `particle(name)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    particle("texte", attach = "none", attachId = 0, duration = 1)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| nom | `name` | texte |  | écrit dans le bloc |
| cible | `entity` | entité |  | optionnel |
| pos | `pos` | vecteur |  | optionnel |
| attach | `attach` | texte | `follow` | écrit dans le bloc, choix: `none`, `follow`, `point` |
| attachId | `attachId` | entier | `0` | de 0 à 63 |
| durée | `duration` | nombre | `1` | de 0 à 30 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **nom** (`name`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **cible** (`entity`, entité). Le fil peut rester vide.
- **pos** (`pos`, vecteur). Le fil peut rester vide.
- **attach** (`attach`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `follow`. Valeurs prévues: `none`, `follow`, `point`.
- **attachId** (`attachId`, entier). Sans fil bleu, le défaut est utilisé. Défaut: `0`. Borné de 0 à 63.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0 à 30.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
