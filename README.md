# Rivals BP, documentation

Site Docusaurus en français. Une page par bloc, avec ses entrées, ses sorties, ses bornes et son verbe. Hébergé sur GitHub Pages : https://realshavkat.github.io/rivals-bp-docs/

## Mettre à jour

Depuis ce dossier, après un changement dans le module (nouveaux blocs, verbes, broches) :

```powershell
.\sync.ps1
```

Le script relit `../ievele/gamemodes/mangarp/gamemode/modules/rivalsbp`, régénère les pages dans `site/docs/blocs`, reconstruit le site dans `docs/`, puis pousse. Pages republie tout seul.

Si le dépôt du jeu n'est pas à côté :

```powershell
$env:RIVALS_BP_ROOT = "C:\chemin\vers\ievele"
python generate.py
cd site
npm run build
```
