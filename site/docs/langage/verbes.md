---
title: Verbes
sidebar_position: 1
description: Chaque mot de la vue Code, et le bloc qu'il devient.
---

# Verbes

Un verbe est un raccourci. Il devient un bloc. La liste est relue dans le module.

## aim

Direction de visée.

Bloc: [`Player.AimDirection`](/blocs/player/player-aimdirection).

Arguments: aucun argument obligatoire.

## anim

Joue une animation.

Bloc: [`Anim.Play`](/blocs/animation/anim-play).

Arguments: `sequence`.

## apply

Applique un statut.

Bloc: [`Status.Apply`](/blocs/status/status-apply).

Arguments: `target`, `status`, `duration`.

## ball

Ballon du joueur (ball, hasBall).

Bloc: [`Ball.Get`](/blocs/ball/ball-get).

Arguments: aucun argument obligatoire.

## call

Déclenche un événement custom.

Bloc: [`Flow.CallEvent`](/blocs/flow/flow-callevent).

Arguments: `name`.

## cancel

Arrête l'exécution.

Bloc: [`Flow.Cancel`](/blocs/flow/flow-cancel).

Arguments: `reason`.

## chance

Vrai avec une probabilité en %.

Bloc: [`Math.Chance`](/blocs/math/math-chance).

Arguments: `percent`.

## cue

Effet de la bibliothèque (particule + son + secousse).

Bloc: [`Step.Cue`](/blocs/step/step-cue).

Arguments: `name`.

## damage

Inflige des dégâts bornés.

Bloc: [`Combat.Damage`](/blocs/combat/combat-damage).

Arguments: `target`, `amount`.

## dash

Dash avec effet.

Bloc: [`Action.Dash`](/blocs/action/action-dash).

Arguments: `direction`.

## find_around

Cibles dans un rayon.

Bloc: [`Target.FindInSphere`](/blocs/targeting/target-findinsphere).

Arguments: `center`, `radius`.

## find_ball

Ballon dans le cône de visée.

Bloc: [`Target.FindBallInCone`](/blocs/targeting/target-findballincone).

Arguments: `range`, `angle`.

## find_target

Cible la plus proche dans le cône de visée.

Bloc: [`Target.FindPlayerInCone`](/blocs/targeting/target-findplayerincone).

Arguments: `range`, `angle`.

## freeze

Fige un joueur.

Bloc: [`Player.Freeze`](/blocs/movement/player-freeze).

Arguments: `duration`.

## get

Lit une variable.

Bloc: [`Var.Get`](/blocs/variables/var-get).

Arguments: `name`.

## guided_pass

Passe guidée vers une cible.

Bloc: [`Ball.GuidedPass`](/blocs/ball/ball-guidedpass).

Arguments: `target`.

## hit

Fenêtre de frappe : portée, dégâts, étourdissement.

Bloc: [`Action.Hit`](/blocs/action/action-hit).

Arguments: `range`.

## hitbox

Agrandit la hitbox.

Bloc: [`Player.SetHitboxMultiplier`](/blocs/player/player-sethitboxmultiplier).

Arguments: `value`, `duration`.

## impact

Tir complet : animation, attente, frappe, effets.

Bloc: [`Action.Impact`](/blocs/action/action-impact).

Arguments: `power`.

## launch

Lâche le ballon et le frappe.

Bloc: [`Ball.Launch`](/blocs/ball/ball-launch).

Arguments: `force`.

## lock

Bloque les déplacements.

Bloc: [`Movement.Lock`](/blocs/movement/movement-lock).

Arguments: `duration`.

## notify

Message au joueur.

Bloc: [`Player.Notify`](/blocs/ui/player-notify).

Arguments: `text`.

## particle

Joue une particule.

Bloc: [`FX.Particle`](/blocs/cosmetic/fx-particle).

Arguments: `name`.

## pass

Passe directe vers une cible.

Bloc: [`Ball.StraightPass`](/blocs/ball/ball-straightpass).

Arguments: `target`.

## projectile

Projectile physique dans l'axe de visée.

Bloc: [`Step.Projectile`](/blocs/step/step-projectile).

Arguments: `speed`.

## recover

Récupération : ralenti pendant N secondes.

Bloc: [`Step.Recover`](/blocs/step/step-recover).

Arguments: `seconds`.

## refund

Rembourse coût et cooldown.

Bloc: [`Skill.Refund`](/blocs/skill/skill-refund).

Arguments: aucun argument obligatoire.

## release_ball

Lâche le ballon sans le frapper.

Bloc: [`Ball.Release`](/blocs/ball/ball-release).

Arguments: aucun argument obligatoire.

## require

Condition de lancement (remboursement si échec).

Bloc: [`Step.Require`](/blocs/step/step-require).

Arguments: `condition`.

## root

Immobilise une cible.

Bloc: [`Status.Apply`](/blocs/status/status-apply).

Arguments: `target`, `duration`.

## set

Enregistre une variable.

Bloc: [`Var.Set`](/blocs/variables/var-set).

Arguments: `name`, `value`.

## shake

Secousse de caméra.

Bloc: [`FX.ScreenShake`](/blocs/cosmetic/fx-screenshake).

Arguments: `pos`.

## shoot

Tir puissant du ballon porté.

Bloc: [`Ball.PowerShot`](/blocs/ball/ball-powershot).

Arguments: `power`.

## slow

Ralentit une cible.

Bloc: [`Status.Apply`](/blocs/status/status-apply).

Arguments: `target`, `duration`, `magnitude`.

## sound

Joue un son.

Bloc: [`FX.Sound`](/blocs/cosmetic/fx-sound).

Arguments: `name`.

## speed

Multiplie la vitesse (buff / debuff).

Bloc: [`Movement.SpeedModifier`](/blocs/movement/movement-speedmodifier).

Arguments: `multiplier`, `duration`.

## steal

Vole le ballon d'une cible.

Bloc: [`Ball.Steal`](/blocs/ball/ball-steal).

Arguments: `victim`.

## stun

Étourdit une cible.

Bloc: [`Status.Apply`](/blocs/status/status-apply).

Arguments: `target`, `duration`.

## take_ball

Ramasse le ballon libre le plus proche.

Bloc: [`Ball.TakeNearby`](/blocs/ball/ball-takenearby).

Arguments: `radius`.

## teleport

Téléporte (distance bornée).

Bloc: [`Player.SetPos`](/blocs/movement/player-setpos).

Arguments: `pos`.

## wait

Attend N secondes.

Bloc: [`Flow.Delay`](/blocs/flow/flow-delay).

Arguments: `seconds`.

## windup

Préparation : animation, cue, verrou, puis attente.

Bloc: [`Step.Windup`](/blocs/step/step-windup).

Arguments: `seconds`.

## zone

Zone qui ralentit et draine autour du lanceur.

Bloc: [`Zone.SlowAura`](/blocs/zone/zone-slowaura).

Arguments: `radius`, `duration`.
