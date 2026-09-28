---
title: Déclencheurs du langage
sidebar_position: 3
description: Les noms on cast, on hit, et le bloc événement derrière.
---

# Déclencheurs du langage

Dans la vue Code, `on cast` réveille un bloc événement. Chaque nom est expliqué dans [Exemples](/langage/exemples).

## ball_lost

Bloc: [`Event.OnBallLost`](/blocs/events/event-onballlost).


```text
on ball_lost {
    notify("déclenché")
}
```

## ball_possess

Bloc: [`Event.OnBallPossess`](/blocs/events/event-onballpossess).


```text
on ball_possess {
    notify("déclenché")
}
```

## cancel

Bloc: [`Event.OnCancel`](/blocs/events/event-oncancel).


```text
on cancel {
    notify("déclenché")
}
```

## cast

Bloc: [`Event.OnSkillCast`](/blocs/events/event-onskillcast).


```text
on cast {
    notify("déclenché")
}
```

## event

Bloc: [`Event.Custom`](/blocs/events/event-custom).


```text
on event("signal") {
    notify("déclenché")
}
```

## flow_off

Bloc: [`Event.OnFlowDeactivate`](/blocs/events/event-onflowdeactivate).


```text
on flow_off {
    notify("déclenché")
}
```

## flow_on

Bloc: [`Event.OnFlowActivate`](/blocs/events/event-onflowactivate).


```text
on flow_on {
    notify("déclenché")
}
```

## hit

Bloc: [`Event.OnHit`](/blocs/events/event-onhit).


```text
on hit {
    notify("déclenché")
}
```

## input

Bloc: `Macro.Input`.

## key

Bloc: [`Event.OnKeyPress`](/blocs/events/event-onkeypress).


```text
on key("jump") {
    notify("déclenché")
}
```

## key_release

Bloc: [`Event.OnKeyRelease`](/blocs/events/event-onkeyrelease).


```text
on key_release("jump") {
    notify("déclenché")
}
```

## land

Bloc: [`Event.OnLand`](/blocs/events/event-onland).


```text
on land {
    notify("déclenché")
}
```

## state

Bloc: [`Event.OnStateChanged`](/blocs/events/event-onstatechanged).


```text
on state {
    notify("déclenché")
}
```

## tackle

Bloc: [`Event.OnTackleAttempt`](/blocs/events/event-ontackleattempt).


```text
on tackle {
    notify("déclenché")
}
```

## test

Bloc: [`Event.OnTest`](/blocs/events/event-ontest).


```text
on test {
    notify("déclenché")
}
```
