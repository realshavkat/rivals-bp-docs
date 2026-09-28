---
sidebar_position: 1
title: Ouvrir le studio
description: Mode développeur et propriétaire, puis Gestion ou la touche B.
---

# Ouvrir le studio

Deux portes. Les deux vérifient la même chose.

## Conditions

1. Ton SteamID64 est dans la liste des propriétaires de Gestion.
2. En jeu, console : `dev 1`.

Sans `dev 1`, l'onglet Studio, les boutons TESTER et la page Rivals BP restent cachés. Le serveur refuse aussi.

## Depuis Gestion

Console : `gestion`. Onglet **Rivals BP**.

## Depuis les techniques

Touche `B`. Choisis une technique. Bouton **ÉDITEUR**. L'onglet **Studio** liste les techniques créées dans l'éditeur.

Il n'y a plus de commande joueur `bl_rbp`. En console serveur seulement : `rbp_status` et `rbp_reload`.

## Après une mise à jour

- Fichiers serveur (lancement, blocs, accès) : recharge le gamemode.
- Fichiers de l'éditeur : ferme le studio et rouvre-le. Le client reçoit un nouveau paquet.
