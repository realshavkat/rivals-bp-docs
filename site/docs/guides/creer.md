---
sidebar_position: 2
title: Créer une technique
description: Une notification, un test, puis la publication.
---

# Créer une technique

Le plus court chemin est une notification. Si le texte s'affiche, le studio, le graphe et le test fonctionnent.

## Skill rapide

1. En haut, **Rapide**.
2. Type : **Notification**.
3. Nom : `alerte_test` (lettres, chiffres, `_`, commence par une lettre).
4. **Créer le skill**.

Deux blocs sont déjà reliés : quand le sort part, puis afficher un texte. Le joueur du second bloc est le lanceur.

## Tester

Sauvegarde, puis **Tester** ou `F5`. Tu dois voir le texte. Pas de ballon, pas de cible, pas de coût.

Un test ignore les anciennes conditions Lua (ballon, position, cible), le gel, le tir en cours et l'étourdissement. Un vrai lancement, hors test, les respecte encore.

## Rendre la technique jouable

1. **Valider** (`Ctrl+Entrée`). Corrige la liste Problèmes.
2. **Publier**. L'ancienne version est archivée, avec une empreinte SHA-256.
3. Visibilité **Test** (développeurs propriétaires) ou **Public** (tout le monde).

Tant que ce n'est pas publié en Public, les joueurs ne l'ont pas. Le brouillon n'est jamais joué.

## La même chose en Code

```
skill "alerte_test" {
    on cast {
        notify("Technique lancée")
    }
}
```

Le verbe `notify` est le bloc [Player.Notify](/blocs/ui/player-notify).
