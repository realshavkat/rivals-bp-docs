---
sidebar_position: 4
title: "Ball.GuidedPass"
sidebar_label: "GuidedPass"
description: "Passe guidée vers un coéquipier (BL.SoccerSkill.GuidedPass)."
---

# Passe guidée vers un coéquipier (BL.SoccerSkill.GuidedPass)

`Ball.GuidedPass`

Passe guidée vers un coéquipier (BL.SoccerSkill.GuidedPass).

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`guided_pass`](/langage/verbes#guided_pass) : `guided_pass(target)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **4** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    guided_pass("texte", player = caster, speed = 1200)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| cible | `target` | entité |  |  |
| vitesse | `speed` | nombre | `1200` | de 900 à 4000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| passed | `passed` | oui/non |  |  |
| ball | `ball` | entité |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **cible** (`target`, entité). Relie un fil bleu.
- **vitesse** (`speed`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1200`. Borné de 900 à 4000.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **passed** (`passed`, oui/non). Relie un fil bleu.
- **ball** (`ball`, entité). Relie un fil bleu.
