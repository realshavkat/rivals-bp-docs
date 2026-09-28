---
sidebar_position: 5
title: "Ball.HitWindow"
sidebar_label: "HitWindow"
description: "Fenêtre de frappe du Skill Kit : le client signale un contact, le serveur le revalide (cône, portée, type)."
---

# HitWindow

`Ball.HitWindow`

Fenêtre de frappe du Skill Kit : le client signale un contact, le serveur le revalide (cône, portée, type).

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **3** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Ball.HitWindow(player = caster, mode = "ball", range = 180, cone = 40)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  |  |
| cible | `mode` | texte | `player` | écrit dans le bloc, choix: `ball`, `player`, `any` |
| portée | `range` | nombre | `180` | de 16 à 2000 |
| angle | `cone` | nombre | `40` | de 5 à 180 |
| durée | `duration` | nombre | `0.4` | de 0.05 à 3 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| touche | `hit` | flux |  |  |
| cible | `target` | entité |  |  |
| raté | `miss` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Relie un fil bleu.
- **cible** (`mode`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `player`. Valeurs prévues: `ball`, `player`, `any`.
- **portée** (`range`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `180`. Borné de 16 à 2000.
- **angle** (`cone`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `40`. Borné de 5 à 180.
- **durée** (`duration`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.4`. Borné de 0.05 à 3.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **touche** (`hit`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **cible** (`target`, entité). Relie un fil bleu.
- **raté** (`miss`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
