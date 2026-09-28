---
sidebar_position: 11
title: "Event.OnSkillCast"
sidebar_label: "OnSkillCast"
description: "Point d'entrée : la technique vient d'être lancée (coût et cooldown déjà appliqués)."
---

# Quand le sort part

`Event.OnSkillCast`

Point d'entrée : la technique vient d'être lancée (coût et cooldown déjà appliqués).

Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui.

Présent seulement sur: technique.

Il se réveille sur l'événement `OnSkillCast`.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
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
| lanceur | `caster` | joueur |  |  |
| niveau | `level` | entier |  |  |
| cible | `target` | quelconque |  |  |

## Détail

- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **lanceur** (`caster`, joueur). Relie un fil bleu.
- **niveau** (`level`, entier). Relie un fil bleu.
- **cible** (`target`, quelconque). Relie un fil bleu.
