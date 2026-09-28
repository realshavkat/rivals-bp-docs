---
sidebar_position: 1
title: "Trigger.OnNextSkillAttempt"
sidebar_label: "OnNextSkillAttempt"
description: "À la prochaine tentative d'une AUTRE technique encore en recharge, relance ce graphe sur l'événement custom donné (a = id de la technique, b = recharge restante). Un seul déclencheur en attente par joueur et par graphe ; aucune exécution n'est gardée ouverte."
---

# OnNextSkillAttempt

`Trigger.OnNextSkillAttempt`

À la prochaine tentative d'une AUTRE technique encore en recharge, relance ce graphe sur l'événement custom donné (a = id de la technique, b = recharge restante). Un seul déclencheur en attente par joueur et par graphe ; aucune exécution n'est gardée ouverte.

Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Trigger.OnNextSkillAttempt(event = "texte", ignoreSelf = true)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| event | `event` | texte |  | écrit dans le bloc |
| ignoreSelf | `ignoreSelf` | oui/non | `oui` |  |
| joueur | `player` | joueur |  | optionnel |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **event** (`event`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **ignoreSelf** (`ignoreSelf`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **joueur** (`player`, joueur). Le fil peut rester vide.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
