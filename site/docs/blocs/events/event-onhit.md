---
sidebar_position: 7
title: "Event.OnHit"
sidebar_label: "OnHit"
description: "Un node de cette exécution a touché une cible (vol, dégâts...)."
---

# Un node de cette exécution a touché une cible (vol, dégâts...)

`Event.OnHit`

Un node de cette exécution a touché une cible (vol, dégâts...).

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Il se réveille sur l'événement `OnHit`.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on hit {
    notify("déclenché")
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

Aucune.

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| cible | `target` | entité |  |  |

## Détail

- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **cible** (`target`, entité). Relie un fil bleu.
