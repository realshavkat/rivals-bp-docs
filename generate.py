import os
import re
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
IEVELE = os.environ.get("RIVALS_BP_ROOT", os.path.normpath(os.path.join(ROOT, "..", "ievele")))
MODULE = os.path.join(IEVELE, "gamemodes", "mangarp", "gamemode", "modules", "rivalsbp")
DOCS = os.path.join(ROOT, "site", "docs")

TYPE_FR = {
    "exec": "flux",
    "bool": "oui/non",
    "number": "nombre",
    "int": "entier",
    "string": "texte",
    "vector": "vecteur",
    "angle": "angle",
    "entity": "entité",
    "player": "joueur",
    "table": "liste",
    "any": "quelconque",
}

CAT_FR = {
    "Events": "Déclencheurs",
    "Flow": "Enchaînement",
    "Logic": "Logique",
    "Math": "Maths",
    "Vector": "Vecteurs",
    "Movement": "Mouvement",
    "Player": "Joueur",
    "Ball": "Ballon",
    "Combat": "Combat",
    "FX": "Effets visuels",
    "Anim": "Animations",
    "Animation": "Animations",
    "Status": "Statuts",
    "Target": "Ciblage",
    "Targeting": "Ciblage",
    "Entity": "Entités",
    "Entities": "Entités",
    "Skill": "Technique",
    "Action": "Actions",
    "Balance": "Équilibrage",
    "Conditions": "Conditions",
    "Cosmetic": "Apparence",
    "Debug": "Débogage",
    "Input": "Touches",
    "Rules": "Règles",
    "Step": "Étapes",
    "Test": "Test",
    "Trigger": "Déclencheurs liés",
    "UI": "Interface",
    "Variables": "Variables",
    "Zone": "Zones",
    "Misc": "Divers",
}

CAT_BLURB = {
    "Action": "Une action de jeu entière dans un seul bloc: tir, dash, frappe.",
    "Events": "Le bloc qui démarre le graphe. Rien ne se branche devant.",
    "Flow": "L'ordre: attendre, choisir, répéter.",
    "Ball": "Lire ou frapper le ballon.",
    "Player": "Le joueur: position, endurance, message, drapeau.",
    "Movement": "Déplacement, vitesse, gel.",
    "Status": "Étourdir, ralentir, immobiliser.",
    "FX": "Son, particule, caméra.",
    "Anim": "Animations du personnage.",
    "Animation": "Animations du personnage.",
    "UI": "Textes et barres vus par le joueur.",
    "Math": "Nombres: addition, hasard, chance.",
    "Logic": "Oui et non, combinés.",
    "Vector": "Positions et directions.",
    "Conditions": "Questions dont la réponse est oui ou non.",
    "Targeting": "Chercher un joueur ou un ballon.",
    "Target": "Chercher un joueur ou un ballon.",
    "Skill": "Le lancement en cours: lanceur, niveau, paramètre.",
    "Variables": "Garder une valeur pour plus tard.",
    "Balance": "Valeurs prévues pour l'équilibrage.",
    "Step": "Étapes toutes faites: préparation, effet, projectile.",
    "Zone": "Une zone autour du lanceur.",
    "Combat": "Dégâts.",
    "Cosmetic": "Ce que les autres voient, sans changer la règle.",
    "Input": "Attendre une touche.",
    "Trigger": "Réagir au prochain essai de technique.",
}

CAT_ORDER = [
    "Events", "Flow", "Action", "Step", "Ball", "Player", "Movement", "Status",
    "Combat", "Zone", "Targeting", "Target", "Conditions", "Logic", "Math",
    "Vector", "Variables", "Skill", "UI", "FX", "Anim", "Animation", "Cosmetic",
    "Input", "Trigger", "Balance", "Rules", "Entities", "Entity", "Debug", "Test", "Misc",
]

BINARY_DOC = {
    "Math.Add": "Additionne a et b.",
    "Math.Sub": "Soustrait b de a.",
    "Math.Mul": "Multiplie a par b.",
    "Math.Div": "Divise a par b. Si b vaut 0, le résultat est 0.",
    "Math.Min": "Le plus petit des deux nombres.",
    "Math.Max": "Le plus grand des deux nombres.",
}

GRAPH_FR = {
    "skill": "technique",
    "flow": "flow",
    "macro": "macro",
    "test": "test",
}


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def slug(text):
    text = text.lower()
    for a, b in (("é", "e"), ("è", "e"), ("ê", "e"), ("à", "a"), ("ù", "u"), ("ô", "o"), ("î", "i"), ("ï", "i"), ("ç", "c")):
        text = text.replace(a, b)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "bloc"


def lua_string(text, i):
    quote = text[i]
    i += 1
    out = []
    while i < len(text):
        c = text[i]
        if c == "\\":
            out.append(text[i + 1] if i + 1 < len(text) else "")
            i += 2
            continue
        if c == quote:
            return "".join(out), i + 1
        out.append(c)
        i += 1
    return "".join(out), i


def match_brace(text, i):
    depth = 0
    while i < len(text):
        c = text[i]
        if c == "-" and i + 1 < len(text) and text[i + 1] == "-":
            i = text.find("\n", i)
            if i < 0:
                return len(text) - 1
        elif c in ('"', "'"):
            _, i = lua_string(text, i)
            continue
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return len(text) - 1


def consts_of(text):
    found = {}
    for m in re.finditer(r"C\.(\w+)\s*=\s*(-?\d+(?:\.\d+)?)", text):
        found[m.group(1)] = m.group(2)
    return found


def eval_expr(expr, consts):
    expr = expr.strip().rstrip(",")
    out = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c in ('"', "'"):
            s, i = lua_string(expr, i)
            out.append(s)
            continue
        if expr.startswith("..", i):
            i += 2
            continue
        if c.isspace():
            i += 1
            continue
        m = re.match(r"C\.(\w+)", expr[i:])
        if m:
            out.append(str(consts.get(m.group(1), m.group(0))))
            i += m.end()
            continue
        i += 1
    return "".join(out).strip()


def string_list(body):
    return re.findall(r'"((?:\\.|[^"\\])*)"', body)


def map_keys(body):
    keys = []
    i = 0
    while i < len(body):
        if body[i] in ('"', "'"):
            _, i = lua_string(body, i)
            continue
        m = re.match(r"\[((?:\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'))\]\s*=", body[i:])
        if m:
            raw = m.group(1)
            keys.append(lua_string(raw, 0)[0])
            i += m.end()
            continue
        m = re.match(r"([A-Za-z_]\w*)\s*=", body[i:])
        if m and m.group(1) not in ("local", "function", "return"):
            keys.append(m.group(1))
            i += m.end()
            continue
        i += 1
    return keys


def locals_of(text):
    tables = {}
    i = 0
    depth = 0
    while i < len(text):
        c = text[i]
        if c == "-" and i + 1 < len(text) and text[i + 1] == "-":
            i = text.find("\n", i)
            if i < 0:
                break
            continue
        if c in ('"', "'"):
            _, i = lua_string(text, i)
            continue
        if c == "{":
            depth += 1
            i += 1
            continue
        if c == "}":
            depth = max(0, depth - 1)
            i += 1
            continue
        if depth == 0:
            m = re.match(r"local\s+([A-Za-z_]\w*)\s*=\s*", text[i:])
            if m:
                j = i + m.end()
                if j < len(text) and text[j] == "{":
                    end = match_brace(text, j)
                    body = text[j + 1 : end]
                    listed = string_list(body)
                    tables[m.group(1)] = listed if listed else map_keys(body)
                    i = end + 1
                    continue
                g = re.match(r"table\.GetKeys\(\s*([A-Za-z_]\w*)\s*\)", text[j:])
                if g and g.group(1) in tables:
                    tables[m.group(1)] = list(tables[g.group(1)])
                    i = j + g.end()
                    continue
        i += 1
    return tables


def cue_names(text):
    m = re.search(r"Cues\.LIBRARY\s*=\s*\{", text)
    if not m:
        return []
    end = match_brace(text, m.end() - 1)
    return map_keys(text[m.end() : end])


def field_expr(body, field):
    m = re.search(r"\b" + field + r"\s*=\s*", body)
    if not m:
        return None
    i = m.end()
    if i < len(body) and body[i] == "{":
        end = match_brace(body, i)
        return body[i : end + 1]
    if i < len(body) and body[i] in ('"', "'"):
        start = i
        while i < len(body):
            while i < len(body) and body[i].isspace():
                i += 1
            if i < len(body) and body[i] in ('"', "'"):
                _, i = lua_string(body, i)
                continue
            if body.startswith("..", i):
                i += 2
                continue
            ident = re.match(r"C\.\w+", body[i:])
            if ident:
                i += ident.end()
                continue
            break
        return body[start:i].strip()
    m2 = re.match(r"-?\d+(?:\.\d+)?|true|false|[A-Za-z_][\w.]*", body[i:])
    return m2.group(0) if m2 else None


def parse_default(raw):
    if raw is None:
        return None
    raw = raw.strip()
    if raw in ("true", "false"):
        return "oui" if raw == "true" else "non"
    if raw[:1] in ('"', "'"):
        return lua_string(raw, 0)[0]
    if re.match(r"-?\d+(\.\d+)?$", raw):
        if raw in ("1000000", "1e6"):
            return "1000000"
        if raw in ("-1000000", "-1e6"):
            return "-1000000"
        return raw
    return None


def resolve_enum(raw, tables, extra):
    if not raw:
        return []
    raw = raw.strip()
    if raw.startswith("{"):
        return string_list(raw)
    name = raw.split(".")[-1]
    if name in tables:
        return tables[name]
    if name in extra:
        return extra[name]
    if raw in extra:
        return extra[raw]
    return []


def parse_pin(chunk, tables, extra, num_mode):
    chunk = chunk.strip()
    m = re.match(r'num\(\s*"([^"]+)"(?:\s*,\s*(-?\d+(?:\.\d+)?))?(?:\s*,\s*(-?[\w.]+))?(?:\s*,\s*(-?[\w.]+))?\s*\)', chunk)
    if m:
        name, default, minv, maxv = m.group(1), m.group(2), m.group(3), m.group(4)
        pin = {"name": name, "type": "number", "default": default or "0"}
        if num_mode == 2:
            pin["min"] = "-1000000"
            pin["max"] = "1000000"
        else:
            pin["min"] = parse_default(minv) or "-1000000"
            pin["max"] = parse_default(maxv) or "1000000"
            if minv in ("-BIG", "-1e6"):
                pin["min"] = "-1000000"
            if maxv in ("BIG", "1e6"):
                pin["max"] = "1000000"
        return pin
    name = field_expr(chunk, "name")
    typ = field_expr(chunk, "type")
    if not name or not typ or name[0] not in ('"', "'"):
        return None
    pin = {"name": lua_string(name, 0)[0], "type": lua_string(typ, 0)[0]}
    default = parse_default(field_expr(chunk, "default"))
    if default is not None:
        pin["default"] = default
    for bound in ("min", "max"):
        raw = field_expr(chunk, bound)
        if raw and re.match(r"-?\d+(\.\d+)?$", raw.strip()):
            pin[bound] = raw.strip()
        elif raw and raw.strip() in ("BIG", "1e6"):
            pin[bound] = "1000000"
        elif raw and raw.strip() in ("-BIG", "-1e6"):
            pin[bound] = "-1000000"
    if re.search(r"\boptional\s*=\s*true", chunk):
        pin["optional"] = True
    if re.search(r"\bliteralOnly\s*=\s*true", chunk):
        pin["literalOnly"] = True
    enum = resolve_enum(field_expr(chunk, "enum"), tables, extra)
    if enum:
        pin["enum"] = enum
    return pin


def split_pins(raw, tables, extra, num_mode):
    if not raw or not raw.startswith("{"):
        return []
    inner = raw[1:-1]
    pins = []
    i = 0
    while i < len(inner):
        if inner[i] in ('"', "'"):
            _, i = lua_string(inner, i)
            continue
        m = re.match(r"num\(", inner[i:])
        if m:
            depth = 0
            j = i
            while j < len(inner):
                if inner[j] == "(":
                    depth += 1
                elif inner[j] == ")":
                    depth -= 1
                    if depth == 0:
                        j += 1
                        break
                j += 1
            pin = parse_pin(inner[i:j], tables, extra, num_mode)
            if pin:
                pins.append(pin)
            i = j
            continue
        if inner[i] == "{":
            end = match_brace(inner, i)
            pin = parse_pin(inner[i : end + 1], tables, extra, num_mode)
            if pin:
                pins.append(pin)
            i = end + 1
            continue
        i += 1
    return pins


def parse_nodes(path, consts, extra):
    text = read(path)
    tables = locals_of(text)
    cues = cue_names(text)
    if cues:
        extra = dict(extra)
        extra["NAMES"] = cues
    num_mode = 4 if re.search(r"function num\(name,\s*default,\s*minv", text) else 2
    nodes = []
    for m in re.finditer(r'Reg\(\s*"([^"]+)"\s*,\s*\{', text):
        start = m.end() - 1
        end = match_brace(text, start)
        body = text[start : end + 1]
        kind = m.group(1)
        desc_raw = field_expr(body, "description")
        desc = eval_expr(desc_raw, consts) if desc_raw else ""
        cat_raw = field_expr(body, "category")
        category = lua_string(cat_raw, 0)[0] if cat_raw and cat_raw[0] in ('"', "'") else "Misc"
        event = field_expr(body, "event")
        if event and event[0] in ('"', "'"):
            event = lua_string(event, 0)[0]
        else:
            event = None
        graphs = string_list(field_expr(body, "graphTypes") or "")
        cost = field_expr(body, "cost")
        node = {
            "kind": kind,
            "category": category,
            "description": desc,
            "event": event,
            "graphs": graphs,
            "latent": bool(re.search(r"\blatent\s*=\s*true", body)),
            "pure": "pure = function" in body or "pure=function" in body,
            "has_ply": "plyOf(" in body,
            "cost": int(cost) if cost and cost.isdigit() else None,
            "inputs": split_pins(field_expr(body, "inputs"), tables, extra, num_mode),
            "outputs": split_pins(field_expr(body, "outputs"), tables, extra, num_mode),
        }
        nodes.append(node)
    for m in re.finditer(r'binary\(\s*"([^"]+)"', text):
        kind = m.group(1)
        nodes.append({
            "kind": kind,
            "category": "Math",
            "description": BINARY_DOC.get(kind, ""),
            "event": None,
            "graphs": [],
            "latent": False,
            "pure": True,
            "has_ply": False,
            "cost": None,
            "inputs": [
                {"name": "a", "type": "number", "default": "0", "min": "-1000000", "max": "1000000"},
                {"name": "b", "type": "number", "default": "0", "min": "-1000000", "max": "1000000"},
            ],
            "outputs": [{"name": "result", "type": "number"}],
        })
    return nodes


def simple_map(text, name):
    m = re.search(r"local\s+" + name + r"\s*=\s*\{", text)
    if not m:
        return {}
    end = match_brace(text, m.end() - 1)
    body = text[m.end() : end]
    out = {}
    for a, b, c in re.findall(r'(?:\["([^"]+)"\]|([A-Za-z_]\w*))\s*=\s*"((?:\\.|[^"\\])*)"', body):
        out[a or b] = c
    return out


def verbs_of(text):
    block = re.search(r"L\.VERBS\s*=\s*\{(.*?)\n\}", text, re.S)
    if not block:
        return []
    rows = []
    for entry in re.split(r"\n\t(?=\w+\s*=)", "\n" + block.group(1)):
        name = re.match(r"\s*(\w+)\s*=", entry)
        kind = re.search(r'kind\s*=\s*"([^"]+)"', entry)
        doc = re.search(r'doc\s*=\s*"([^"]*)"', entry)
        args = re.search(r"args\s*=\s*\{([^}]*)\}", entry)
        if name and kind and doc:
            argn = re.findall(r'"([^"]+)"', args.group(1)) if args else []
            rows.append({"name": name.group(1), "kind": kind.group(1), "doc": doc.group(1), "args": argn})
    rows.sort(key=lambda r: r["name"])
    return rows


def events_of(text):
    block = re.search(r"L\.EVENTS\s*=\s*\{(.*?)\}", text, re.S)
    if not block:
        return []
    rows = [{"name": a, "kind": b} for a, b in re.findall(r'(\w+)\s*=\s*"([^"]+)"', block.group(1))]
    rows.sort(key=lambda r: r["name"])
    return rows


def pin_label(name, pins):
    return pins.get(name) or name.replace("_", " ")


def md_cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ")


def fmt_default(pin):
    if "default" not in pin:
        return ""
    val = pin["default"]
    if pin["type"] in ("string",):
        return "`" + val + "`" if val != "" else "`vide`"
    return "`" + val + "`"


def pin_notes(pin):
    notes = []
    if pin.get("optional"):
        notes.append("optionnel")
    if pin.get("literalOnly"):
        notes.append("écrit dans le bloc")
    if "min" in pin or "max" in pin:
        notes.append("de %s à %s" % (pin.get("min", "…"), pin.get("max", "…")))
    if pin.get("enum"):
        shown = pin["enum"][:12]
        extra = "…" if len(pin["enum"]) > 12 else ""
        notes.append("choix: " + ", ".join("`" + x + "`" for x in shown) + extra)
    return ", ".join(notes)


def explain_pin(pin, pins, direction, has_ply):
    label = pin_label(pin["name"], pins)
    typ = TYPE_FR.get(pin["type"], pin["type"])
    if pin["type"] == "exec":
        if direction == "in":
            return "**%s** (`%s`). Le fil blanc arrive ici. C'est l'ordre: sans ce fil, le bloc ne démarre pas." % (label, pin["name"])
        return "**%s** (`%s`). Sors d'ici en fil blanc pour enchaîner un autre bloc." % (label, pin["name"])
    bits = ["**%s** (`%s`, %s)." % (label, pin["name"], typ)]
    if pin.get("literalOnly"):
        bits.append("Tu l'écris dans le bloc. Un fil ne peut pas la remplacer.")
    elif pin.get("optional") and pin["type"] == "player" and has_ply:
        bits.append("Tu peux laisser le fil vide: le bloc prend le lanceur.")
    elif pin.get("optional"):
        bits.append("Le fil peut rester vide.")
    elif "default" in pin:
        bits.append("Sans fil bleu, le défaut est utilisé.")
    else:
        bits.append("Relie un fil bleu.")
    if "default" in pin:
        shown = "vide" if pin["default"] == "" else pin["default"]
        bits.append("Défaut: `%s`." % shown)
    if "min" in pin or "max" in pin:
        bits.append("Borné de %s à %s." % (pin.get("min", "…"), pin.get("max", "…")))
    if pin.get("enum"):
        bits.append("Valeurs prévues: %s." % ", ".join("`" + x + "`" for x in pin["enum"]))
    return " ".join(bits)


def role_of(node):
    if node["event"]:
        return "Déclencheur. Il démarre une branche tout seul. Tu ne branches rien devant lui."
    if node["pure"]:
        return "Calcul. Il ne s'enchaîne pas. Un autre bloc lit sa sortie avec un fil bleu, et la valeur est recalculée à ce moment-là."
    if node["category"] == "Flow":
        return "Enchaînement. Il décide quelle suite blanche part, et quand."
    if node["latent"]:
        return "Action qui peut attendre. La suite blanche part plus tard, quand l'attente est finie."
    return "Action. Le fil blanc entre, le bloc fait son effet, le fil blanc sort."


def page_for(node, pins, plain, verb, url):
    kind = node["kind"]
    short = kind.split(".")[-1]
    desc = node["description"] or (verb["doc"] if verb else "") or ""
    if kind in plain:
        title = plain[kind]
    elif desc and len(desc) <= 80:
        title = desc.rstrip(".")
    else:
        title = short
    lines = [
        "---",
        "sidebar_position: 1",
        'title: "%s"' % kind.replace('"', ""),
        'sidebar_label: "%s"' % short.replace('"', ""),
        "description: %s" % json_escape(desc or title),
        "---",
        "",
        "# %s" % (title[:1].upper() + title[1:]),
        "",
        "`%s`" % kind,
        "",
        desc or "Le module ne donne pas de phrase pour ce bloc. Le rôle se lit sur les entrées et les sorties.",
        "",
        role_of(node),
        "",
    ]
    if verb:
        args = ", ".join(verb["args"]) if verb["args"] else ""
        lines.append("Dans la vue Code, le verbe est [`%s`](/langage/verbes#%s)%s." % (verb["name"], verb["name"], (" : `" + verb["name"] + "(" + args + ")`") if args else ""))
        lines.append("")
    if node["pure"]:
        lines.append("Pas de fil blanc sur ce bloc. On ne fait que lire le résultat.")
        lines.append("")
    elif not node["event"]:
        lines.append("Le fil blanc est l'ordre. Le fil bleu est une valeur. Un fil bleu gagne sur le défaut.")
        lines.append("")
    if node["graphs"]:
        lines.append("Présent seulement sur: %s." % ", ".join(GRAPH_FR.get(g, g) for g in node["graphs"]))
        lines.append("")
    if node["event"]:
        lines.append("Il se réveille sur l'événement `%s`." % node["event"])
        lines.append("")
    if node["cost"] and node["cost"] != 1:
        lines.append("Chaque passage consomme **%d** dans le budget d'exécution (le défaut est 1)." % node["cost"])
        lines.append("")
    lines.append("## Entrées")
    lines.append("")
    lines.extend(pin_table(node["inputs"], pins))
    lines.append("")
    lines.append("## Sorties")
    lines.append("")
    lines.extend(pin_table(node["outputs"], pins))
    lines.append("")
    lines.append("## Détail")
    lines.append("")
    if not node["inputs"] and not node["outputs"]:
        lines.append("Aucune broche déclarée.")
    for pin in node["inputs"]:
        lines.append("- " + explain_pin(pin, pins, "in", node["has_ply"]))
    for pin in node["outputs"]:
        lines.append("- " + explain_pin(pin, pins, "out", node["has_ply"]))
    lines.append("")
    return "\n".join(lines)


def json_escape(text):
    text = " ".join((text or "").split())
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def pin_table(pins_list, labels):
    if not pins_list:
        return ["Aucune."]
    rows = ["| Sur le graphe | Interne | Type | Défaut | Notes |", "| --- | --- | --- | --- | --- |"]
    for pin in pins_list:
        rows.append("| %s | `%s` | %s | %s | %s |" % (
            md_cell(pin_label(pin["name"], labels)),
            pin["name"],
            TYPE_FR.get(pin["type"], pin["type"]),
            fmt_default(pin),
            md_cell(pin_notes(pin)),
        ))
    return rows


def escape_mdx(text):
    parts = re.split(r"(`[^`]*`)", text)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(part)
        else:
            out.append(part.replace("{", "&#123;").replace("}", "&#125;").replace("<", "&lt;"))
    return "".join(out)


def protect(md):
    end = md.find("\n---\n", 3)
    if not md.startswith("---") or end < 0:
        return escape_mdx(md)
    return md[: end + 5] + escape_mdx(md[end + 5 :])


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main():
    if not os.path.isdir(MODULE):
        raise SystemExit("module introuvable: " + MODULE)
    server = os.path.join(MODULE, "server")
    core = read(os.path.join(MODULE, "shared", "sh_rbp_core.lua"))
    steps = read(os.path.join(MODULE, "lang", "sh_rbp_steps.lua"))
    simple = read(os.path.join(MODULE, "editor", "cl_rbp_simple.lua"))
    consts = consts_of(core)
    extra = {"STATUS_NAMES": string_list(re.search(r"RBP\.STATUS_NAMES\s*=\s*\{([^}]*)\}", core).group(1))}
    pins = simple_map(simple, "PINS")
    plain = simple_map(simple, "PLAIN")
    nodes = []
    for name in sorted(os.listdir(server)):
        if name.startswith("sv_rbp_nodes") and name.endswith(".lua"):
            nodes.extend(parse_nodes(os.path.join(server, name), consts, extra))
    by_kind = {}
    for node in nodes:
        by_kind[node["kind"]] = node
    nodes = [by_kind[k] for k in sorted(by_kind)]
    verb_rows = verbs_of(steps)
    verb_by_kind = {}
    for row in verb_rows:
        verb_by_kind.setdefault(row["kind"], row)
    blocs = os.path.join(DOCS, "blocs")
    if os.path.isdir(blocs):
        shutil.rmtree(blocs)
    groups = {}
    for node in nodes:
        groups.setdefault(node["category"], []).append(node)
    order = {name: i for i, name in enumerate(CAT_ORDER)}
    cats = sorted(groups, key=lambda c: (order.get(c, 500), c))
    write(os.path.join(blocs, "_category_.json"),
          '{\n  "label": "Blocs",\n  "position": 4,\n  "className": "cat-blocs",\n  "link": {\n    "type": "generated-index",\n    "slug": "/blocs",\n    "description": "Une page par bloc. Choisis une famille, puis le bloc. Le fil blanc est l\'ordre, le fil bleu est une valeur."\n  }\n}\n')
    urls = {}
    for cat in cats:
        folder = slug(cat)
        label = CAT_FR.get(cat, cat)
        pos = order.get(cat, 500)
        blurb = CAT_BLURB.get(cat, "Blocs de la famille %s." % label)
        write(os.path.join(blocs, folder, "_category_.json"),
              '{\n  "label": "%s",\n  "position": %d,\n  "className": "cat-%s",\n  "link": {\n    "type": "generated-index",\n    "description": "%s"\n  }\n}\n' % (label.replace('"', ""), pos, folder, blurb.replace('"', "")))
        used = {}
        for i, node in enumerate(sorted(groups[cat], key=lambda n: n["kind"])):
            base = slug(node["kind"])
            file_name = base
            n = 2
            while file_name in used:
                file_name = base + "-" + str(n)
                n += 1
            used[file_name] = True
            url = "/blocs/%s/%s" % (folder, file_name)
            urls[node["kind"]] = url
            body = page_for(node, pins, plain, verb_by_kind.get(node["kind"]), url)
            body = body.replace("sidebar_position: 1\n", "sidebar_position: %d\n" % (i + 1), 1)
            write(os.path.join(blocs, folder, file_name + ".md"), protect(body))
    langage = os.path.join(DOCS, "langage")
    os.makedirs(langage, exist_ok=True)
    write(os.path.join(langage, "_category_.json"),
          '{\n  "label": "Langage",\n  "position": 3,\n  "className": "cat-langage",\n  "link": {\n    "type": "generated-index",\n    "slug": "/langage",\n    "description": "La vue Code écrit le même graphe. Le texte n\'est jamais exécuté comme du Lua."\n  }\n}\n')
    verb_lines = ["---", "title: Verbes", "sidebar_position: 1", "description: Chaque mot de la vue Code, et le bloc qu'il devient.", "---", "", "# Verbes", "", "Un verbe est un raccourci. Il devient un bloc. La liste est relue dans le module.", ""]
    for row in verb_rows:
        url = urls.get(row["kind"], "")
        link = "[`%s`](%s)" % (row["kind"], url) if url else "`%s`" % row["kind"]
        args = ", ".join("`" + a + "`" for a in row["args"]) if row["args"] else "aucun argument obligatoire"
        verb_lines += ["## %s" % row["name"], "", row["doc"], "", "Bloc: %s." % link, "", "Arguments: %s." % args, ""]
    write(os.path.join(langage, "verbes.md"), protect("\n".join(verb_lines)))
    ev_lines = ["---", "title: Déclencheurs du langage", "sidebar_position: 2", "description: Les noms on cast, on hit, et le bloc événement derrière.", "---", "", "# Déclencheurs du langage", "", "Dans la vue Code, `on cast` réveille un bloc événement.", ""]
    for row in events_of(steps):
        url = urls.get(row["kind"], "")
        link = "[`%s`](%s)" % (row["kind"], url) if url else "`%s`" % row["kind"]
        ev_lines += ["## %s" % row["name"], "", "Bloc: %s." % link, ""]
    write(os.path.join(langage, "declencheurs.md"), protect("\n".join(ev_lines)))
    missing = [n["kind"] for n in nodes if not n["inputs"] and not n["outputs"] and not n["event"]]
    print("%d blocs, %d familles, %d verbes" % (len(nodes), len(cats), len(verb_rows)))
    if missing:
        print("sans broches:", ", ".join(missing))


if __name__ == "__main__":
    main()
