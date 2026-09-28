---
sidebar_position: 6
title: "Event.OnFlowDeactivate"
sidebar_label: "OnFlowDeactivate"
description: "OnFlowDeactivate"
---

# OnFlowDeactivate

`Event.OnFlowDeactivate`

Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Présent seulement sur: flow.

Il se réveille sur l'événement `OnFlowDeactivate`.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on flow_off {
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
| joueur | `player` | joueur |  |  |

## Détail

- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **joueur** (`player`, joueur). Relie un fil bleu.
