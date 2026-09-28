---
sidebar_position: 14
title: "Ball.Steal"
sidebar_label: "Steal"
description: "Vole le ballon d'une cible (refusé sur un gardien). Déclenche Event.OnHit."
---

# Vole le ballon d'une cible (refusé sur un gardien). Déclenche Event.OnHit

`Ball.Steal`

Vole le ballon d'une cible (refusé sur un gardien). Déclenche Event.OnHit.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`steal`](/langage/verbes#steal) : `steal(victim)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **3** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    steal("texte", player = caster)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| victim | `victim` | entité |  |  |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| stolen | `stolen` | oui/non |  |  |
| keeper | `keeper` | oui/non |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **victim** (`victim`, entité). Relie un fil bleu.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **stolen** (`stolen`, oui/non). Relie un fil bleu.
- **keeper** (`keeper`, oui/non). Relie un fil bleu.
