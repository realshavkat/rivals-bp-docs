---
sidebar_position: 4
title: "Step.Require"
sidebar_label: "Require"
description: "Condition de lancement. Si elle échoue : sortie 'failed' si reliée, sinon remboursement + message + arrêt."
---

# Require

`Step.Require`

Condition de lancement. Si elle échoue : sortie 'failed' si reliée, sinon remboursement + message + arrêt.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Dans la vue Code, le verbe est [`require`](/langage/verbes#require) : `require(condition)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    require("has_ball")
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| condition | `condition` | texte |  | écrit dans le bloc, choix: `has_ball`, `no_ball`, `on_ground`, `in_air`, `keeper`, `not_keeper` |
| message | `message` | texte |  | optionnel, écrit dans le bloc |
| joueur | `player` | joueur |  | optionnel |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| failed | `failed` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **condition** (`condition`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Valeurs prévues: `has_ball`, `no_ball`, `on_ground`, `in_air`, `keeper`, `not_keeper`.
- **message** (`message`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **joueur** (`player`, joueur). Le fil peut rester vide.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **failed** (`failed`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
