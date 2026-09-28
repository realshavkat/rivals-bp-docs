---
title: Exemples
sidebar_position: 1
sidebar_label: Exemples
description: Le langage d'étapes, morceau par morceau, avec un exemple à chaque fois.
---

# Exemples

La vue Code écrit le même graphe que les blocs. Le texte n'est jamais exécuté comme du Lua. Un mot inconnu est une erreur.

Chaque fiche de [verbe](/langage/verbes) a aussi son exemple court. Ici, c'est la grammaire, une idée à la fois.

## Une technique qui ne fait qu'un message

```text
skill "ping" {
    name = "Ping"

    on cast {
        notify("ça part")
    }
}
```

`skill "ping"` ouvre une technique. L'identifiant entre guillemets est l'id. `name` est le titre affiché. `on cast` est le départ, quand le joueur lance. `notify` est le verbe du bloc message. Les étapes d'un bloc s'écrivent l'une sous l'autre, dans l'ordre du fil blanc.

## L'en-tête

```text
skill "tir_courbe" {
    name = "Tir Courbé"
    style = "isagi"
    rank = "A"
    cooldown = 8
    stamina = 25
}
```

Chaque ligne `clé = valeur` est une métadonnée. `cooldown` est le temps avant de pouvoir relancer. `stamina` est le coût d'endurance. `style` et `rank` classent la technique. Rien de tout ça n'est une étape.

Les types de fichier sont `skill`, `flow`, `macro` et `test`. Un flow se réveille avec `on flow_on`, pas avec `on cast`.

## Un paramètre que tu règles

```text
params {
    -- Puissance du tir, lue par @power
    power: number = 1400, min = 0, max = 8000
}

on cast {
    shoot(@power, lift = 60)
}
```

`params` déclare des valeurs de la fiche. `power: number = 1400` donne le type, puis le défaut. `min` et `max` bornent. Le commentaire au-dessus est gardé.

`@power` lit ce paramètre. `shoot(1400, lift = 60)` est la même chose, en dur. Le premier argument sans nom suit l'ordre du verbe. Ici, le premier de `shoot` est `power`. La suite se nomme: `lift = 60`.

`env = "Power"` relie le paramètre à la clé d'équilibrage du même nom. L'équilibrage continue de s'appliquer à chaud.

## Une condition avant de partir

```text
skill "controle" {
    name = "Contrôle"
    requires = {"has_ball", "on_ground"}

    on cast {
        windup(0.3)
    }
}
```

`requires` ajoute des `require(...)` au début de `on cast`. Si une condition rate, la technique est remboursée et s'arrête.

Valeurs prévues: `has_ball`, `no_ball`, `on_ground`, `in_air`, `keeper`, `not_keeper`.

Tu peux aussi l'écrire en étape:

```text
on cast {
    require("has_ball")
    windup(0.3)
}
```

## Préparer, frapper, récupérer

```text
on cast {
    windup(0.4, cue = "charge")
    shoot(@power, lift = 60)
    recover(0.35)
}
```

`windup` prépare: attente, animation, effet. `shoot` frappe. `recover` ralentit le joueur à la fin. L'ordre des lignes est l'ordre d'exécution.

`wait(0.2)` attend sans le costume d'une préparation. `impact(12000)` est un tir entier dans un seul verbe: animation, attente, frappe, effet, caméra.

## Choisir une branche

```text
on cast {
    if chance(40) {
        notify("réussi")
        dash("forward")
    } else {
        notify("raté")
        recover(0.4)
    }
}
```

`if` ouvre deux suites. `chance(40)` est vrai environ 40 fois sur 100. Rien ne s'écrit après le `if` dans le même bloc: les deux chemins continuent chacun de leur côté. La suite commune se met dans les deux branches, ou avec `goto`.

## Touche, ou rate

```text
on cast {
    strike: hit(160, stun = true) {
        hit {
            cue("impact_lourd", entity = strike.target)
        }
        miss {
            recover(0.4)
        }
    }
}
```

`hit` a deux sorties blanches. Le bloc entre accolades nomme ces sorties: `hit` et `miss`.

`strike:` est une étiquette. Elle donne l'id `strike` à l'étape. `strike.target` lit la sortie `target` de cette étape. Sans étiquette, l'id est fabriqué (`hit_1`, `hit_2`).

## Répéter

```text
on cast {
    salve: repeat 3 every 0.2 {
        shoot(800)
    }
    notify("terminé")
}
```

`repeat 3 every 0.2` lance le bloc trois fois, avec 0.2 s entre chaque tour. Les lignes après le bloc partent quand la série est finie. `salve.index` est le numéro du tour.

```text
on cast {
    loop from 1 to 5 {
        wait(0.1)
    }
}
```

`loop from 1 to 5` compte. Le moteur s'arrête à 64 tours.

## Lire une valeur, puis s'en servir

```text
data {
    visee = aim()
    cible = find_target(900, 40)
}

on cast {
    if cible.found {
        pass(cible.target)
    } else {
        shoot(2000)
    }
}
```

`data` pose des calculs. Ils n'ont pas de fil blanc. `aim()` et `find_target` se recalculent quand une étape les lit.

`cible.found` et `cible.target` sont des sorties du bloc. `pass` envoie le ballon vers le joueur trouvé.

Le lanceur n'a pas besoin d'être écrit. Une entrée joueur vide prend celui qui a lancé. `lock(0.5)` suffit, pas `lock(player = caster)`. `caster` existe quand tu veux le nommer.

## Un vecteur et un calcul

```text
data {
    haut = {0, 0, 80}
    force = (niveau * 100 + 500)
}

on cast {
    launch(force)
}
```

`{0, 0, 80}` est un vecteur, x y z. `(niveau * 100 + 500)` est une expression. Dedans: nombres, `niveau`, `pos`, `avant`, `droite`, `haut`, et `+ - * /`.

## Après la frappe, ou quand le ballon part

```text
on cast {
    shoot(3000)
}

on hit {
    notify("touché")
}

on land {
    recover(0.2)
}

on ball_lost {
    cancel("ballon perdu")
}
```

Chaque `on` est un départ séparé. `on cast` est le lancement. `on hit` part quand une frappe de cette technique touche. `on land` quand le lanceur retouche le sol. `on ball_lost` quand il n'a plus le ballon.

Les autres départs:

```text
on key("jump") {
    dash("up")
}

on key_release("jump") {
    notify("touche relâchée")
}

on ball_possess {
    notify("ballon en main")
}

on tackle {
    notify("tacle essayé")
}

on state {
    notify("statut changé")
}

on cancel {
    notify("technique coupée")
}

on flow_on {
    notify("flow allumé")
}

on flow_off {
    notify("flow éteint")
}
```

`on key` et `on key_release` prennent le nom de la touche. `on flow_on` sert dans un fichier `flow`, pas dans une technique.

## Un signal que tu nommes

```text
on cast {
    call("apres_tir")
}

on event("apres_tir") {
    cue("impact_lourd")
}
```

`call("apres_tir")` réveille `on event("apres_tir")` dans le même graphe. Le nom est libre, les deux doivent être identiques.

## Garder un nombre

```text
vars {
    charge: number = 0
}

on cast {
    set("charge", 1)
    notify("chargé")
}
```

`vars` déclare une variable du graphe. `set` écrit, `get` relit. `scope = "player"` la garde sur le joueur entre deux lancements.

```text
vars {
    charge: number = 0, scope = "player"
}

data {
    deja = get("charge")
}
```

## Rejoindre une étape déjà écrite

```text
on cast {
    if chance(50) {
        dash("left")
        goto suite
    } else {
        dash("right")
        goto suite
    }
}

detached {
    suite: recover(0.3)
}
```

`goto suite` relie la ligne courante à l'étape étiquetée `suite`. `detached` est une chaîne sans déclencheur: on n'y arrive que par un `goto`.

`goto poll.stop` vise une entrée précise (`stop`, `reset`, `open`, `close`) quand le bloc en a plusieurs.

## Le nom complet, quand il n'y a pas de verbe

```text
on cast {
    Ball.SetBone(bone = "ball_fx3")
}
```

Si le catalogue n'a pas de verbe court, écris `Categorie.Nom(...)`. Les arguments se nomment comme les broches du bloc. La liste des verbes courts est sur [Verbes](/langage/verbes).

## Une technique qui reprend une autre

```text
skill "tir_courbe_fort" {
    extends = "tir_courbe"

    params {
        power: number = 2200
    }

    overrides = {"shot.power" = 5000}
}
```

`extends` copie le graphe de base. Tu changes la méta, les paramètres, et des entrées précises avec `overrides`. La clé `"shot.power"` vise l'entrée `power` de l'étape étiquetée `shot`. Tu ne réécris pas les étapes. Quatre niveaux maximum. Un cycle est refusé.

## Un commentaire qui reste

```text
on cast {
    -- tenue une demi-seconde, le temps de l'animation
    windup(0.5)
}
```

`--` commente jusqu'à la fin de la ligne. Placé juste au-dessus d'une étape, d'un paramètre ou d'une métadonnée, il est gardé dans le graphe et réaffiché.

## Ce que le texte refuse

```text
ligne 14 : verbe inconnu 'shot'                          → vouliez-vous dire shoot ?
ligne 15 : étape 'shoot_1' : entrée 'powr' inexistante   → vouliez-vous dire power ?
```

La vue Code donne la ligne, l'étape, la valeur reçue, la valeur attendue, et une piste quand elle en a une. Le texte ne lance pas de Lua, ne lit pas de fichier, n'appelle pas le réseau.
