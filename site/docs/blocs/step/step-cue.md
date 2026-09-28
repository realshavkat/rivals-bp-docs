---
sidebar_position: 1
title: "Step.Cue"
sidebar_label: "Cue"
description: "Joue un effet de la bibliothèque (particule, son, secousse) sur une entité ou à une position."
---

# Cue

`Step.Cue`

Joue un effet de la bibliothèque (particule, son, secousse) sur une entité ou à une position.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`cue`](/langage/verbes#cue) : `cue(name)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    cue("charge")
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| nom | `name` | texte |  | écrit dans le bloc, choix: `charge`, `label`, `sound`, `level`, `charge_aura`, `label`, `sound`, `level`, `particle`, `particleTime`, `flash`, `label`… |
| cible | `entity` | entité |  | optionnel |
| pos | `pos` | vecteur |  | optionnel |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **nom** (`name`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Valeurs prévues: `charge`, `label`, `sound`, `level`, `charge_aura`, `label`, `sound`, `level`, `particle`, `particleTime`, `flash`, `label`, `particle`, `particleTime`, `impact`, `label`, `sound`, `level`, `impact_lourd`, `label`, `sound`, `level`, `shake`, `amplitude`, `frequency`, `duration`, `radius`, `tir`, `label`, `sound`, `level`, `whoosh`, `label`, `sound`, `level`, `whoosh_fort`, `label`, `sound`, `level`, `dash`, `label`, `sound`, `level`, `dash_barou`, `label`, `sound`, `level`, `particle`, `particleTime`, `vitesse`, `label`, `sound`, `level`, `dribble`, `label`, `sound`, `level`, `controle`, `label`, `sound`, `level`, `passe`, `label`, `sound`, `level`, `aura_isagi`, `label`, `particle`, `particleTime`, `aura_nagi`, `label`, `particle`, `particleTime`, `aura_shidou`, `label`, `particle`, `particleTime`, `aura_otoya`, `label`, `particle`, `particleTime`, `secousse`, `label`, `shake`, `amplitude`, `frequency`, `duration`, `radius`.
- **cible** (`entity`, entité). Le fil peut rester vide.
- **pos** (`pos`, vecteur). Le fil peut rester vide.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
