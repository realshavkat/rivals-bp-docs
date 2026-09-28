---
slug: /
sidebar_position: 1
title: Accueil
description: Par où commencer pour créer une technique dans Rivals BP.
---

import Link from "@docusaurus/Link";

# Rivals BP

L'éditeur pour créer des techniques de Blue Lock. Tu poses des blocs, tu les relies, tu testes sur toi, puis tu publies.

<div className="jump">
  <Link className="jump-card c-cyan" to="/guides/ouvrir"><b>Guides</b><span>Ouvrir, créer, tester, publier</span></Link>
  <Link className="jump-card c-violet" to="/blocs"><b>Blocs</b><span>Une page par bloc, par famille</span></Link>
  <Link className="jump-card c-amber" to="/langage/verbes"><b>Langage</b><span>Les verbes de la vue Code</span></Link>
</div>

Le graphe est la source de vérité. La vue Code est le même graphe, écrit en langage d'étapes. Ce texte n'est jamais exécuté comme du Lua.

## En dix minutes

1. [Ouvre le studio](/guides/ouvrir). Mode développeur, et SteamID propriétaire.
2. [Crée une notification](/guides/creer). Un brouillon n'est joué par personne.
3. Relie le fil blanc (l'ordre) et le fil bleu (la valeur). [Lire l'écran](/guides/ecran).
4. Teste avec F5. Ça part sur toi, sans endurance ni ballon obligatoire.
5. Publie, puis choisis Test ou Public.
6. Ouvre [Blocs](/blocs) : une page par bloc, avec ses entrées, ses sorties et ses limites.

## Comment lire une page de bloc

Chaque bloc a la même fiche.

- Le nom en haut est celui du graphe (`Action.Impact`).
- **Entrées** : ce que tu branches devant.
- **Sorties** : ce que tu branches derrière.
- **Détail** : une phrase par broche, le défaut, les bornes, les choix.

Le fil blanc est l'ordre (`exec`, `then`, `suite`). Le fil bleu est une valeur. Un fil bleu remplace le défaut.
