---
title: Verbes
sidebar_position: 2
description: Chaque mot de la vue Code, et le bloc qu'il devient.
---

# Verbes

Un verbe est un raccourci. Il devient un bloc. Pour la grammaire, ouvre [Exemples](/langage/exemples). La liste est relue dans le module.

## aim

Direction de visée.

Bloc: [`Player.AimDirection`](/blocs/player/player-aimdirection).

Arguments: aucun argument obligatoire.


```text
data {
    valeur = aim(player = caster, flat = false)
}
```

## anim

Joue une animation.

Bloc: [`Anim.Play`](/blocs/animation/anim-play).

Arguments: `sequence`.


```text
on cast {
    anim("texte", player = caster, rate = 1, loop = false)
}
```

## apply

Applique un statut.

Bloc: [`Status.Apply`](/blocs/status/status-apply).

Arguments: `target`, `status`, `duration`.


```text
on cast {
    apply(caster, "slow", 1, magnitude = 0.5)
}
```

## ball

Ballon du joueur (ball, hasBall).

Bloc: [`Ball.Get`](/blocs/ball/ball-get).

Arguments: aucun argument obligatoire.


```text
data {
    valeur = ball(player = caster)
}
```

## call

Déclenche un événement custom.

Bloc: [`Flow.CallEvent`](/blocs/flow/flow-callevent).

Arguments: `name`.


```text
on cast {
    call("texte")
}
```

## cancel

Arrête l'exécution.

Bloc: [`Flow.Cancel`](/blocs/flow/flow-cancel).

Arguments: `reason`.


```text
on cast {
    cancel("Flow.Cancel")
}
```

## chance

Vrai avec une probabilité en %.

Bloc: [`Math.Chance`](/blocs/math/math-chance).

Arguments: `percent`.


```text
data {
    valeur = chance(50)
}
```

## cue

Effet de la bibliothèque (particule + son + secousse).

Bloc: [`Step.Cue`](/blocs/step/step-cue).

Arguments: `name`.


```text
on cast {
    cue("charge")
}
```

## damage

Inflige des dégâts bornés.

Bloc: [`Combat.Damage`](/blocs/combat/combat-damage).

Arguments: `target`, `amount`.


```text
on cast {
    damage("texte", 5)
}
```

## dash

Dash avec effet.

Bloc: [`Action.Dash`](/blocs/action/action-dash).

Arguments: `direction`.


```text
on cast {
    dash("forward", speed = 900, duration = 0.28)
}
```

## find_around

Cibles dans un rayon.

Bloc: [`Target.FindInSphere`](/blocs/targeting/target-findinsphere).

Arguments: `center`, `radius`.


```text
data {
    valeur = find_around({0, 0, 0}, 200, filter = "targets", max = 8)
}
```

## find_ball

Ballon dans le cône de visée.

Bloc: [`Target.FindBallInCone`](/blocs/targeting/target-findballincone).

Arguments: `range`, `angle`.


```text
data {
    valeur = find_ball(150, 60, player = caster)
}
```

## find_target

Cible la plus proche dans le cône de visée.

Bloc: [`Target.FindPlayerInCone`](/blocs/targeting/target-findplayerincone).

Arguments: `range`, `angle`.


```text
data {
    valeur = find_target(300, 60, player = caster, requireSight = true)
}
```

## freeze

Fige un joueur.

Bloc: [`Player.Freeze`](/blocs/movement/player-freeze).

Arguments: `duration`.


```text
on cast {
    freeze(1, player = caster, moveTypeNone = false)
}
```

## get

Lit une variable.

Bloc: [`Var.Get`](/blocs/variables/var-get).

Arguments: `name`.


```text
data {
    valeur = get("texte")
}
```

## guided_pass

Passe guidée vers une cible.

Bloc: [`Ball.GuidedPass`](/blocs/ball/ball-guidedpass).

Arguments: `target`.


```text
on cast {
    guided_pass("texte", player = caster, speed = 1200)
}
```

## hit

Fenêtre de frappe : portée, dégâts, étourdissement.

Bloc: [`Action.Hit`](/blocs/action/action-hit).

Arguments: `range`.


```text
on cast {
    hit(180, mode = "ball", cone = 40, duration = 0.35)
}
```

## hitbox

Agrandit la hitbox.

Bloc: [`Player.SetHitboxMultiplier`](/blocs/player/player-sethitboxmultiplier).

Arguments: `value`, `duration`.


```text
on cast {
    hitbox(1.5, 1, player = caster)
}
```

## impact

Tir complet : animation, attente, frappe, effets.

Bloc: [`Action.Impact`](/blocs/action/action-impact).

Arguments: `power`.


```text
on cast {
    impact(12000, sequence = "player_shoot_highpower_v0_bton", windup = 0.4, lift = 220)
}
```

## launch

Lâche le ballon et le frappe.

Bloc: [`Ball.Launch`](/blocs/ball/ball-launch).

Arguments: `force`.


```text
on cast {
    launch(2000, player = caster, lift = 50, powerShot = false)
}
```

## lock

Bloque les déplacements.

Bloc: [`Movement.Lock`](/blocs/movement/movement-lock).

Arguments: `duration`.


```text
on cast {
    lock(0.5, player = caster)
}
```

## notify

Message au joueur.

Bloc: [`Player.Notify`](/blocs/ui/player-notify).

Arguments: `text`.


```text
on cast {
    notify("texte", player = caster, kind = "info", duration = 3)
}
```

## particle

Joue une particule.

Bloc: [`FX.Particle`](/blocs/cosmetic/fx-particle).

Arguments: `name`.


```text
on cast {
    particle("texte", attach = "none", attachId = 0, duration = 1)
}
```

## pass

Passe directe vers une cible.

Bloc: [`Ball.StraightPass`](/blocs/ball/ball-straightpass).

Arguments: `target`.


```text
on cast {
    pass("texte", player = caster, speed = 900)
}
```

## projectile

Projectile physique dans l'axe de visée.

Bloc: [`Step.Projectile`](/blocs/step/step-projectile).

Arguments: `speed`.


```text
on cast {
    projectile(1500, model = "models/props_junk/rock001a.mdl", lifetime = 3)
}
```

## recover

Récupération : ralenti pendant N secondes.

Bloc: [`Step.Recover`](/blocs/step/step-recover).

Arguments: `seconds`.


```text
on cast {
    recover(0.3, slow = 0.6)
}
```

## refund

Rembourse coût et cooldown.

Bloc: [`Skill.Refund`](/blocs/skill/skill-refund).

Arguments: aucun argument obligatoire.


```text
on cast {
    refund()
}
```

## release_ball

Lâche le ballon sans le frapper.

Bloc: [`Ball.Release`](/blocs/ball/ball-release).

Arguments: aucun argument obligatoire.


```text
on cast {
    release_ball(player = caster, hideClient = false, nextTouch = 0.2)
}
```

## require

Condition de lancement (remboursement si échec).

Bloc: [`Step.Require`](/blocs/step/step-require).

Arguments: `condition`.


```text
on cast {
    require("has_ball")
}
```

## root

Immobilise une cible.

Bloc: [`Status.Apply`](/blocs/status/status-apply).

Arguments: `target`, `duration`.


```text
on cast {
    root(caster, 1, status = "slow", magnitude = 0.5)
}
```

## set

Enregistre une variable.

Bloc: [`Var.Set`](/blocs/variables/var-set).

Arguments: `name`, `value`.


```text
on cast {
    set("texte", "texte")
}
```

## shake

Secousse de caméra.

Bloc: [`FX.ScreenShake`](/blocs/cosmetic/fx-screenshake).

Arguments: `pos`.


```text
on cast {
    shake({0, 0, 0}, amplitude = 5, frequency = 5, duration = 0.5)
}
```

## shoot

Tir puissant du ballon porté.

Bloc: [`Ball.PowerShot`](/blocs/ball/ball-powershot).

Arguments: `power`.


```text
on cast {
    shoot(2000, player = caster, lift = 50, particleTime = 1.2)
}
```

## slow

Ralentit une cible.

Bloc: [`Status.Apply`](/blocs/status/status-apply).

Arguments: `target`, `duration`, `magnitude`.


```text
on cast {
    slow(caster, 1, 0.5, status = "slow")
}
```

## sound

Joue un son.

Bloc: [`FX.Sound`](/blocs/cosmetic/fx-sound).

Arguments: `name`.


```text
on cast {
    sound("texte", level = 80, pitch = 100, volume = 1)
}
```

## speed

Multiplie la vitesse (buff / debuff).

Bloc: [`Movement.SpeedModifier`](/blocs/movement/movement-speedmodifier).

Arguments: `multiplier`, `duration`.


```text
on cast {
    speed(1.5, 1, player = caster)
}
```

## steal

Vole le ballon d'une cible.

Bloc: [`Ball.Steal`](/blocs/ball/ball-steal).

Arguments: `victim`.


```text
on cast {
    steal("texte", player = caster)
}
```

## stun

Étourdit une cible.

Bloc: [`Status.Apply`](/blocs/status/status-apply).

Arguments: `target`, `duration`.


```text
on cast {
    stun(caster, 1, status = "slow", magnitude = 0.5)
}
```

## take_ball

Ramasse le ballon libre le plus proche.

Bloc: [`Ball.TakeNearby`](/blocs/ball/ball-takenearby).

Arguments: `radius`.


```text
on cast {
    take_ball(100, player = caster)
}
```

## teleport

Téléporte (distance bornée).

Bloc: [`Player.SetPos`](/blocs/movement/player-setpos).

Arguments: `pos`.


```text
on cast {
    teleport({0, 0, 0}, player = caster, maxDistance = 500)
}
```

## wait

Attend N secondes.

Bloc: [`Flow.Delay`](/blocs/flow/flow-delay).

Arguments: `seconds`.


```text
on cast {
    wait(0.2)
}
```

## windup

Préparation : animation, cue, verrou, puis attente.

Bloc: [`Step.Windup`](/blocs/step/step-windup).

Arguments: `seconds`.


```text
on cast {
    windup(0.4, rate = 1, lock = false, cue = "charge")
}
```

## zone

Zone qui ralentit et draine autour du lanceur.

Bloc: [`Zone.SlowAura`](/blocs/zone/zone-slowaura).

Arguments: `radius`, `duration`.


```text
on cast {
    zone(128, 8, player = caster, slowPercent = 50)
}
```
