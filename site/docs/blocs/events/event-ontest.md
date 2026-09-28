---
sidebar_position: 14
title: "Event.OnTest"
sidebar_label: "OnTest"
description: "OnTest"
---

# OnTest

`Event.OnTest`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Présent seulement sur: test.

Il se réveille sur l'événement `OnTest`.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on test {
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
| a | `a` | quelconque |  |  |

## Détail

- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **a** (`a`, quelconque). Relie un fil bleu.
