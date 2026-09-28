---
sidebar_position: 4
title: "Action.Skill"
sidebar_label: "Skill"
description: "Action du skill. Coche seulement ce que le sort doit faire."
---

# Coche ce que le sort fait

`Action.Skill`

Action du skill. Coche seulement ce que le sort doit faire.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

Chaque passage consomme **6** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
on cast {
    Action.Skill(anim = true, sequence = "player_shoot_highpower_v0_bton", rate = 1, windup = 0.4)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| joueur | `player` | joueur |  | optionnel |
| animation | `anim` | oui/non | `oui` |  |
| animation | `sequence` | texte | `player_shoot_highpower_v0_bton` |  |
| rythme | `rate` | nombre | `1` | de 0.05 à 5 |
| attente | `windup` | nombre | `0.4` | de 0 à 3 |
| dash | `dash` | oui/non | `non` |  |
| direction | `direction` | texte | `forward` | choix: `forward`, `back`, `left`, `right` |
| dashSpeed | `dashSpeed` | nombre | `900` | de 0 à 3000 |
| dashTime | `dashTime` | nombre | `0.25` | de 0.05 à 3 |
| effet | `vfx` | oui/non | `non` |  |
| particule | `particle` | texte | `vide` | optionnel, écrit dans le bloc |
| vfxTime | `vfxTime` | nombre | `1.2` | de 0 à 10 |
| son | `sfx` | oui/non | `non` |  |
| son | `sound` | texte | `vide` | optionnel, écrit dans le bloc |
| tir | `shot` | oui/non | `oui` |  |
| puissance | `power` | nombre | `8000` | de 0 à 100000 |
| hauteur | `lift` | nombre | `80` | de -5000 à 5000 |
| caméra | `shake` | oui/non | `non` |  |
| force caméra | `amplitude` | nombre | `6` | de 0 à 20 |
| bloquer | `lock` | oui/non | `non` |  |
| message | `notify` | oui/non | `non` |  |
| texte | `text` | texte | `Technique lancée` | écrit dans le bloc |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| fini | `finished` | flux |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **joueur** (`player`, joueur). Tu peux laisser le fil vide: le bloc prend le lanceur.
- **animation** (`anim`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **animation** (`sequence`, texte). Sans fil bleu, le défaut est utilisé. Défaut: `player_shoot_highpower_v0_bton`.
- **rythme** (`rate`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.05 à 5.
- **attente** (`windup`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.4`. Borné de 0 à 3.
- **dash** (`dash`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **direction** (`direction`, texte). Sans fil bleu, le défaut est utilisé. Défaut: `forward`. Valeurs prévues: `forward`, `back`, `left`, `right`.
- **dashSpeed** (`dashSpeed`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `900`. Borné de 0 à 3000.
- **dashTime** (`dashTime`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.25`. Borné de 0.05 à 3.
- **effet** (`vfx`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **particule** (`particle`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `vide`.
- **vfxTime** (`vfxTime`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1.2`. Borné de 0 à 10.
- **son** (`sfx`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **son** (`sound`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `vide`.
- **tir** (`shot`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `oui`.
- **puissance** (`power`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `8000`. Borné de 0 à 100000.
- **hauteur** (`lift`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `80`. Borné de -5000 à 5000.
- **caméra** (`shake`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **force caméra** (`amplitude`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `6`. Borné de 0 à 20.
- **bloquer** (`lock`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **message** (`notify`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **texte** (`text`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Défaut: `Technique lancée`.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **fini** (`finished`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
