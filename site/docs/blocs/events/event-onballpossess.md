---
sidebar_position: 3
title: "Event.OnBallPossess"
sidebar_label: "OnBallPossess"
description: "Le lanceur récupère le ballon (réception ou vol)."
---

# Le lanceur récupère le ballon (réception ou vol)

`Event.OnBallPossess`

Le lanceur récupère le ballon (réception ou vol).

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Il se réveille sur l'événement `OnBallPossess`.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on ball_possess {
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
| ball | `ball` | entité |  |  |
| stolen | `stolen` | oui/non |  |  |

## Détail

- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **ball** (`ball`, entité). Relie un fil bleu.
- **stolen** (`stolen`, oui/non). Relie un fil bleu.
