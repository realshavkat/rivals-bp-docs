import os
import re
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "docs")
IEVELE = os.environ.get("RIVALS_BP_ROOT", os.path.normpath(os.path.join(ROOT, "..", "ievele")))
MODULE = os.path.join(IEVELE, "gamemodes", "mangarp", "gamemode", "modules", "rivalsbp")

NAV = [
    ("index.html", "Accueil"),
    ("ouvrir.html", "Ouvrir"),
    ("creer.html", "Créer"),
    ("ecran.html", "L'écran"),
    ("langage.html", "Langage"),
    ("catalogue.html", "Catalogue"),
    ("depannage.html", "Dépannage"),
]


def layout(active, body):
    items = []
    for href, label in NAV:
        cls = "item on" if href == active else "item"
        items.append('<a class="%s" href="%s">%s</a>' % (cls, href, label))
    return """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rivals BP</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="shell">
<nav>
  <span class="brand">Rivals BP<small>Documentation</small></span>
  %s
</nav>
<main>
%s
<footer>Généré depuis le module Rivals BP. Relance <span class="kbd">sync.ps1</span> après un changement.</footer>
</main>
</div>
</body>
</html>
""" % ("\n  ".join(items), body)


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def verbs(text):
    block = re.search(r"L\.VERBS\s*=\s*\{(.*?)\n\}", text, re.S)
    if not block:
        return []
    rows = []
    parts = re.split(r"\n\t(?=\w+\s*=)", "\n" + block.group(1))
    for entry in parts:
        name = re.match(r"\s*(\w+)\s*=", entry)
        doc = re.search(r'doc\s*=\s*"([^"]*)"', entry)
        if name and doc:
            rows.append((name.group(1), doc.group(1)))
    rows.sort(key=lambda r: r[0])
    return rows


def events(text):
    block = re.search(r"L\.EVENTS\s*=\s*\{(.*?)\}", text, re.S)
    if not block:
        return []
    rows = re.findall(r"(\w+)\s*=\s*\"([^\"]+)\"", block.group(1))
    rows.sort(key=lambda r: r[0])
    return rows


def blocks(folder):
    found = []
    if not os.path.isdir(folder):
        return found
    for name in os.listdir(folder):
        if not name.endswith(".lua"):
            continue
        text = read(os.path.join(folder, name))
        parts = re.split(r'\nReg\(\s*"', "\n" + text)
        for part in parts[1:]:
            kind = re.match(r'([^"]+)"', part)
            if not kind:
                continue
            cat = re.search(r'category\s*=\s*"([^"]+)"', part[:2500])
            found.append((kind.group(1), cat.group(1) if cat else "Autre"))
    found.sort(key=lambda r: (r[1], r[0]))
    return found


def table(headers, rows):
    head = "".join("<th>%s</th>" % h for h in headers)
    body = []
    for row in rows:
        body.append("<tr>" + "".join("<td>%s</td>" % c for c in row) + "</tr>")
    return "<table><tr>%s</tr>%s</table>" % (head, "".join(body))


def catalogue():
    steps = os.path.join(MODULE, "lang", "sh_rbp_steps.lua")
    server = os.path.join(MODULE, "server")
    if not os.path.isfile(steps):
        return "<h1>Catalogue</h1><p class='callout bad'>Module introuvable. Définis RIVALS_BP_ROOT vers le dépôt ievele.</p>"
    text = read(steps)
    v = verbs(text)
    e = events(text)
    b = blocks(server)
    parts = [
        "<h1>Catalogue</h1>",
        "<p class='lead'>Relu dans le module à chaque génération. %d verbes, %d déclencheurs, %d blocs.</p>"
        % (len(v), len(e), len(b)),
        "<h2>Verbes</h2>",
        "<p>Ce que tu écris dans la vue Code. Chaque verbe devient un bloc.</p>",
        table(["Verbe", "Effet"], [("<code>%s</code>" % n, d) for n, d in v]),
        "<h2>Déclencheurs</h2>",
        table(["Nom", "Bloc"], [("<code>%s</code>" % n, "<code>%s</code>" % k) for n, k in e]),
        "<h2>Blocs du graphe</h2>",
        "<p>Regroupés par famille. Le préfixe avant le point est le genre.</p>",
        table(["Bloc", "Famille"], [("<code>%s</code>" % k, c) for k, c in b]),
    ]
    return "\n".join(parts)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"))
    shutil.copy(os.path.join(SRC, "style.css"), os.path.join(OUT, "assets", "style.css"))
    pages = os.path.join(SRC, "pages")
    for name in os.listdir(pages):
        if not name.endswith(".html"):
            continue
        body = read(os.path.join(pages, name))
        with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(layout(name, body))
    with open(os.path.join(OUT, "catalogue.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(layout("catalogue.html", catalogue()))
    open(os.path.join(OUT, ".nojekyll"), "w", encoding="utf-8").close()
    print("site écrit dans", OUT)


if __name__ == "__main__":
    main()
