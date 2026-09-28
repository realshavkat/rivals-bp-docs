---
sidebar_position: 8
title: "FX.Sound"
sidebar_label: "Sound"
description: "Joue un son."
---

# Son

`FX.Sound`

Joue un son.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`sound`](/langage/verbes#sound) : `sound(name)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    sound("texte", level = 80, pitch = 100, volume = 1)
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
| niveau | `level` | nombre | `80` | de 20 à 180 |
| pitch | `pitch` | nombre | `100` | de 1 à 255 |
| volume | `volume` | nombre | `1` | de 0 à 1 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **nom** (`name`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **cible** (`entity`, entité). Le fil peut rester vide.
- **pos** (`pos`, vecteur). Le fil peut rester vide.
- **niveau** (`level`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `80`. Borné de 20 à 180.
- **pitch** (`pitch`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `100`. Borné de 1 à 255.
- **volume** (`volume`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0 à 1.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
