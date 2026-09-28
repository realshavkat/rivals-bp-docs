# Rivals BP, documentation

Site en français pour apprendre l'éditeur de techniques. Hébergé gratuitement avec GitHub Pages, dossier `docs/` de la branche `main`.

## Mettre à jour

Depuis ce dossier, après un changement dans le module Rivals BP (verbes, blocs, déclencheurs) :

```powershell
.\sync.ps1
```

Le script relit `../ievele/gamemodes/mangarp/gamemode/modules/rivalsbp`, régénère le catalogue, commit et pousse. GitHub Pages republie le dossier `docs/` de `main` tout seul.

Si le dépôt du jeu n'est pas à côté :

```powershell
$env:RIVALS_BP_ROOT = "C:\chemin\vers\ievele"
python build.py
```

## Pages

Accueil, ouvrir le studio, créer une technique, lire l'écran, langage d'étapes, catalogue généré, dépannage.
