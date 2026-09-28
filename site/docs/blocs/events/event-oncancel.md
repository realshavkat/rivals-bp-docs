---
sidebar_position: 4
title: "Event.OnCancel"
sidebar_label: "OnCancel"
description: "L'exécution est annulée (mort, déconnexion, stun, erreur...). Rien ne peut être planifié ici."
---

# OnCancel

`Event.OnCancel`

L'exécution est annulée (mort, déconnexion, stun, erreur...). Rien ne peut être planifié ici.

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Il se réveille sur l'événement `OnCancel`.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cancel {
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
| reason | `reason` | texte |  |  |

## Détail

- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **reason** (`reason`, texte). Relie un fil bleu.
