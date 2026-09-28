---
sidebar_position: 2
title: "Flow.CallEvent"
sidebar_label: "CallEvent"
description: "Déclenche un Event.Custom du même graphe (synchrone)."
---

# Déclenche un Event.Custom du même graphe (synchrone)

`Flow.CallEvent`

Déclenche un Event.Custom du même graphe (synchrone).

Enchaînement. Il décide quelle suite blanche part, et quand.

Dans la vue Code, le verbe est [`call`](/langage/verbes#call) : `call(name)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    call("texte")
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| nom | `name` | texte |  | écrit dans le bloc |
| a | `a` | quelconque |  | optionnel |
| b | `b` | quelconque |  | optionnel |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **nom** (`name`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **a** (`a`, quelconque). Le fil peut rester vide.
- **b** (`b`, quelconque). Le fil peut rester vide.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
