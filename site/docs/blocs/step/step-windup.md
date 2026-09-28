---
sidebar_position: 5
title: "Step.Windup"
sidebar_label: "Windup"
description: "Préparation : animation, cue et verrou facultatifs, puis attente avant la suite."
---

# Préparation : animation, cue et verrou facultatifs, puis attente avant la suite

`Step.Windup`

Préparation : animation, cue et verrou facultatifs, puis attente avant la suite.

Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie.

Dans la vue Code, le verbe est [`windup`](/langage/verbes#windup) : `windup(seconds)`.

Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| départ | `exec` | flux |  |  |
| secondes | `seconds` | nombre | `0.4` | de 0 à 5 |
| animation | `anim` | texte |  | optionnel, écrit dans le bloc |
| rythme | `rate` | nombre | `1` | de 0.05 à 5 |
| bloquer | `lock` | oui/non | `non` |  |
| cue | `cue` | texte |  | optionnel, écrit dans le bloc, choix: `charge`, `label`, `sound`, `level`, `charge_aura`, `label`, `sound`, `level`, `particle`, `particleTime`, `flash`, `label`… |
| joueur | `player` | joueur |  | optionnel |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| suite | `then` | flux |  |  |
| durée | `duration` | nombre |  |  |

## Détail

- **départ** (`exec`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas.
- **secondes** (`seconds`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `0.4`. Borné de 0 à 5.
- **animation** (`anim`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.
- **rythme** (`rate`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `1`. Borné de 0.05 à 5.
- **bloquer** (`lock`, oui/non). Sans fil bleu, le défaut est utilisé. Défaut: `non`.
- **cue** (`cue`, texte). Tu l'écris dans le bloc. Un fil ne peut pas la remplacer. Valeurs prévues: `charge`, `label`, `sound`, `level`, `charge_aura`, `label`, `sound`, `level`, `particle`, `particleTime`, `flash`, `label`, `particle`, `particleTime`, `impact`, `label`, `sound`, `level`, `impact_lourd`, `label`, `sound`, `level`, `shake`, `amplitude`, `frequency`, `duration`, `radius`, `tir`, `label`, `sound`, `level`, `whoosh`, `label`, `sound`, `level`, `whoosh_fort`, `label`, `sound`, `level`, `dash`, `label`, `sound`, `level`, `dash_barou`, `label`, `sound`, `level`, `particle`, `particleTime`, `vitesse`, `label`, `sound`, `level`, `dribble`, `label`, `sound`, `level`, `controle`, `label`, `sound`, `level`, `passe`, `label`, `sound`, `level`, `aura_isagi`, `label`, `particle`, `particleTime`, `aura_nagi`, `label`, `particle`, `particleTime`, `aura_shidou`, `label`, `particle`, `particleTime`, `aura_otoya`, `label`, `particle`, `particleTime`, `secousse`, `label`, `shake`, `amplitude`, `frequency`, `duration`, `radius`.
- **joueur** (`player`, joueur). Le fil peut rester vide.
- **suite** (`then`). Sors d'ici en fil blanc pour enchaîner un autre bloc.
- **durée** (`duration`, nombre). Relie un fil bleu.
