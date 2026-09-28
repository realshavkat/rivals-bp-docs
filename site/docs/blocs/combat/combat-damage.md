---
sidebar_position: 1
title: "Combat.Damage"
sidebar_label: "Damage"
description: "Inflige des dégâts (bornés) ; déclenche Event.OnHit dans cette exécution."
---

# Inflige des dégâts (bornés) ; déclenche Event.OnHit dans cette exécution

`Combat.Damage`

Inflige des dégâts (bornés) ; déclenche Event.OnHit dans cette exécution.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`damage`](/langage/verbes#damage) : `damage(target, amount)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    damage("texte", 5)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| cible | `target` | entité |  |  |
| amount | `amount` | nombre | `5` | de 0 à 100 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **cible** (`target`, entité). Relie un fil bleu.
- **amount** (`amount`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `5`. Borné de 0 à 100.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
