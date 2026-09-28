---
sidebar_position: 2
title: "Target.FindFreeBall"
sidebar_label: "FindFreeBall"
description: "Premier ballon libre (sans porteur) dans un rayon, même dimension que le lanceur."
---

# FindFreeBall

`Target.FindFreeBall`

Premier ballon libre (sans porteur) dans un rayon, même dimension que le lanceur.

Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là.

Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.

Chaque passage consomme **6** dans le budget d'exécution (le défaut est 1).

## Exemple

Le même bloc, écrit dans la vue Code. Les nombres et les textes sont des valeurs de départ du module, à changer.

```text
data {
    valeur = Target.FindFreeBall(center = {0, 0, 0}, radius = 100)
}
```

La grammaire complète est dans [Exemples](/langage/exemples).

## Entrées

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| center | `center` | vecteur |  |  |
| radius | `radius` | nombre | `100` | de 1 à 2000 |

## Sorties

| Sur le graphe | Interne | Type | Défaut | Notes |
| --- | --- | --- | --- | --- |
| ball | `ball` | entité |  |  |
| found | `found` | oui/non |  |  |

## Détail

- **center** (`center`, vecteur). Relie un fil bleu.
- **radius** (`radius`, nombre). Sans fil bleu, le défaut est utilisé. Défaut: `100`. Borné de 1 à 2000.
- **ball** (`ball`, entité). Relie un fil bleu.
- **found** (`found`, oui/non). Relie un fil bleu.
