# -*- coding: utf-8 -*-
"""Génère le calendrier des cours 2026-2027 (HTML prêt pour impression A4, 2 pages)."""
import json, datetime as dt, calendar, html, pathlib

HERE = pathlib.Path(__file__).parent
data = json.load(open(HERE / 'data.json'))
iso = dt.date.fromisoformat
cours = {iso(d) for d in data["cours"]}
grid = {iso(d) for d in data["grid"]}
vac = [(iso(a), iso(b)) for a, b in data["vac"]]
blocs = [(iso(a), iso(b), n) for a, b, n in data["blocs"]]
sem = [(iso(l), iso(a), iso(b), n) for l, a, b, n in data["sem"]]
start, end = min(cours), max(cours)

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]
JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
ABBR = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.",
        "août", "sept.", "oct.", "nov.", "déc."]
NOMS_VAC = ["Toussaint", "Noël", "Hiver", "Printemps", "Mai"]


def fr(d, court=False):
    return f"{d.day} {ABBR[d.month - 1] if court else MOIS[d.month - 1]} {d.year}"


def fr_jour(d):
    return f"{JOURS[d.weekday()]} {fr(d)}"


def mini_mois(an, mois):
    """Une vignette mensuelle : en-tête, jours de la semaine, cases."""
    nb_cours = sum(1 for d in cours if d.year == an and d.month == mois)
    out = [f'<div class="m">',
           f'<div class="m-h"><span class="m-n">{MOIS[mois-1]}</span>'
           f'<span class="m-y">{an}</span>'
           f'<span class="m-c">{nb_cours or "—"}</span></div>',
           '<div class="g">']
    for j in "LMMJVS":
        out.append(f'<div class="wd">{j}</div>')
    out.append('<div class="wd wd-d">D</div>')

    premier = dt.date(an, mois, 1)
    for _ in range(premier.weekday()):
        out.append('<div class="d d-off"></div>')
    for jour in range(1, calendar.monthrange(an, mois)[1] + 1):
        d = dt.date(an, mois, jour)
        if d in cours:
            cls = "d d-cours"
        elif d not in grid:
            cls = "d d-hors"
        elif d.weekday() == 6:
            cls = "d d-dim"
        else:
            cls = "d d-vac"
        marque = ""
        if d == start or d == end:
            marque = " d-jalon"
        out.append(f'<div class="{cls}{marque}">{jour}</div>')
    out.append('</div></div>')
    return "".join(out)


# ---------- Page 1 : les vignettes mensuelles ----------
mois_liste = []
an, mo = start.year, start.month
while (an, mo) <= (end.year, end.month):
    mois_liste.append((an, mo))
    mo += 1
    if mo == 13:
        mo, an = 1, an + 1

vignettes = "".join(mini_mois(a, m) for a, m in mois_liste)

carte_vac = ['<div class="m m-info"><div class="i-h">Interruptions</div><ul class="i-l">']
for (a, b), nom in zip(vac, NOMS_VAC):
    carte_vac.append(
        f'<li><span class="i-t">{nom}</span>'
        f'<span class="i-d">{a.day} {ABBR[a.month-1]} &rarr; {b.day} {ABBR[b.month-1]}</span>'
        f'<span class="i-n">{(b-a).days+1} j</span></li>')
carte_vac.append(
    '</ul><div class="i-f">'
    '<div><b>Reprise</b> le lendemain de chaque fin de période.</div>'
    "<div>Seule exception&nbsp;: la Toussaint s’achève un vendredi &mdash; "
    'les cours reprennent le <b>samedi 31 octobre</b>.</div>'
    '</div></div>')
carte_vac = "".join(carte_vac)

# ---------- Page 2 : rythme de l’année ----------
alt = []
for i, (a, b, n) in enumerate(blocs):
    alt.append(f'<div class="p p-cours"><div class="p-k">Période {i+1}</div>'
               f'<div class="p-d">{fr(a, True)} &nbsp;&rarr;&nbsp; {fr(b, True)}</div>'
               f'<div class="p-n">{n} jours</div></div>')
    if i < len(vac):
        va, vb = vac[i]
        alt.append(f'<div class="p p-vac"><div class="p-k">{NOMS_VAC[i]}</div>'
                   f'<div class="p-d">{fr(va, True)} &nbsp;&rarr;&nbsp; {fr(vb, True)}</div>'
                   f'<div class="p-n">{(vb-va).days+1} jours</div></div>')
alt = "".join(alt)

lignes_sem = []
for i, (l, a, b, n) in enumerate(sem, 1):
    part = "" if n == 6 else " s-part"
    lignes_sem.append(
        f'<li class="s{part}"><span class="s-n">{i:02d}</span>'
        f'<span class="s-d">{a.day:02d}/{a.month:02d} &ndash; {b.day:02d}/{b.month:02d}</span>'
        f'<span class="s-j">{n} j</span></li>')
lignes_sem = "".join(lignes_sem)

CSS = """
:root{
  --ink:#161a20; --ink-2:#4a525e; --ink-3:#8b93a1;
  --acc:#2b4a7d; --acc-soft:#dce5f4; --acc-line:#b9c9e4;
  --vac:#b8763a; --vac-soft:#f7ece1;
  --rule:#e3e6ec; --paper:#fff;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Liberation Sans","Helvetica Neue",Arial,"DejaVu Sans",sans-serif;
  color:var(--ink);background:var(--paper);-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:297mm;padding:13mm 14mm 10mm;display:flex;flex-direction:column;
  page-break-after:always;overflow:hidden}
.page:last-child{page-break-after:auto}

/* ---- en-tête ---- */
.hd{border-bottom:1.6pt solid var(--ink);padding-bottom:3.2mm;margin-bottom:4mm;
  display:flex;align-items:flex-end;justify-content:space-between;gap:6mm}
.hd-eyebrow{font-size:7pt;letter-spacing:.20em;text-transform:uppercase;color:var(--acc);
  font-weight:700;margin-bottom:1.4mm}
.hd h1{font-family:"Bitstream Charter","Liberation Serif",Georgia,serif;
  font-size:24pt;line-height:1;font-weight:700;letter-spacing:-.01em}
.hd-sub{font-size:8.6pt;color:var(--ink-2);margin-top:1.8mm}
.hd-sub b{color:var(--ink);font-weight:700}
.hd-r{text-align:right;flex-shrink:0}
.hd-big{font-family:"Bitstream Charter","Liberation Serif",Georgia,serif;
  font-size:30pt;line-height:.9;font-weight:700;color:var(--acc)}
.hd-lab{font-size:6.8pt;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);
  font-weight:700;margin-top:1.2mm}

/* ---- bandeau chiffres ---- */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:.6pt solid var(--rule);
  border-radius:1.6mm;overflow:hidden;margin-bottom:3.6mm}
.st{padding:2.6mm 3mm;border-right:.6pt solid var(--rule)}
.st:last-child{border-right:0}
.st-v{font-size:12pt;font-weight:700;line-height:1;letter-spacing:-.01em}
.st-l{font-size:6.6pt;color:var(--ink-2);margin-top:1.1mm;line-height:1.3}

/* ---- légende ---- */
.lg{display:flex;gap:5mm;align-items:center;font-size:7pt;color:var(--ink-2);margin-bottom:3.4mm}
.lg i{display:inline-block;width:3.1mm;height:3.1mm;border-radius:.7mm;margin-right:1.3mm;
  vertical-align:-.5mm;border:.5pt solid var(--rule)}
.lg .k-c{background:var(--acc-soft);border-color:var(--acc-line)}
.lg .k-v{background:#fff;border-color:#c8cdd6}
.lg .k-d{background:#f4f5f7;border-color:#eceef1}
.lg .k-j{background:var(--acc);border-color:var(--acc)}

/* ---- grille des mois ---- */
.mois{display:grid;grid-template-columns:repeat(3,1fr);gap:4.5mm;flex:1;
  grid-auto-rows:1fr;align-content:stretch}
.m{display:flex;flex-direction:column}
.m-h{display:flex;align-items:baseline;gap:1.4mm;border-bottom:.8pt solid var(--ink);
  padding-bottom:1.1mm;margin-bottom:1.4mm}
.m-n{font-size:10.2pt;font-weight:700;text-transform:capitalize;letter-spacing:-.01em}
.m-y{font-size:7pt;color:var(--ink-3);font-weight:700}
.m-c{margin-left:auto;font-size:7.2pt;font-weight:700;color:var(--acc);
  background:var(--acc-soft);border-radius:4mm;padding:.3mm 1.6mm}
.g{display:grid;grid-template-columns:repeat(7,1fr);gap:.6mm}
.wd{font-size:6.4pt;font-weight:700;color:var(--ink-3);text-align:center;padding-bottom:.6mm}
.wd-d{color:#c2c8d2}
.d{font-size:7.8pt;text-align:center;padding:1.35mm 0;border-radius:.8mm;color:var(--ink-2)}
.d-cours{background:var(--acc-soft);color:var(--acc);font-weight:700}
.d-vac{background:#fff;color:var(--ink-3)}
.d-dim{background:#f4f5f7;color:#c2c8d2}
.d-hors{color:#dfe2e7}
.d-off{}
.d-jalon{background:var(--acc);color:#fff;font-weight:700}

/* ---- carte interruptions ---- */
.m-info{grid-column:span 2;background:var(--vac-soft);border-radius:1.8mm;padding:2.6mm 3.2mm;
  display:flex;flex-direction:column}
.i-h{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;font-weight:700;color:var(--vac);
  border-bottom:.8pt solid #e6d3bf;padding-bottom:1.2mm;margin-bottom:1.4mm}
.i-l{list-style:none;columns:2;column-gap:4mm}
.i-l li{display:flex;align-items:baseline;gap:1.4mm;font-size:7.6pt;padding:2.5mm 0;
  break-inside:avoid}
.i-t{font-weight:700;min-width:16mm}
.i-d{color:var(--ink-2)}
.i-n{margin-left:auto;color:var(--vac);font-weight:700;font-size:7pt}
.i-f{margin-top:auto;padding-top:2.2mm;border-top:.8pt solid #e6d3bf;font-size:7pt;
  color:#9c7247;line-height:1.55;display:flex;flex-direction:column;gap:.6mm}
.i-f b{color:var(--vac);font-weight:700}

/* ---- page 2 ---- */
.h2{font-family:"Bitstream Charter","Liberation Serif",Georgia,serif;font-size:14pt;
  font-weight:700;letter-spacing:-.01em;margin-bottom:1mm}
.h2-s{font-size:8pt;color:var(--ink-2);margin-bottom:3.2mm}
.sec{margin-bottom:7mm}
.rythme{display:flex;flex-direction:column;gap:1.5mm}
.p{display:flex;align-items:baseline;gap:3mm;padding:3.1mm 3.4mm;border-radius:1.4mm}
.p-cours{background:var(--acc-soft);color:var(--acc)}
.p-vac{background:var(--vac-soft);color:var(--vac);margin-left:14mm}
.p-k{font-size:8.2pt;font-weight:700;min-width:22mm;letter-spacing:.02em}
.p-d{font-size:9.2pt;font-weight:700;color:var(--ink)}
.p-vac .p-d{font-weight:400;color:var(--ink-2)}
.p-n{margin-left:auto;font-size:7.6pt;font-weight:700}
.sems{list-style:none;columns:3;column-gap:6mm}
.s{display:flex;align-items:baseline;gap:2mm;font-size:8.2pt;padding:1.75mm 1.6mm;
  border-bottom:.5pt solid var(--rule);break-inside:avoid}
.s-n{font-weight:700;color:var(--acc);min-width:6.5mm;font-size:7.4pt}
.s-d{color:var(--ink)}
.s-j{margin-left:auto;color:var(--ink-3);font-size:7pt}
.s-part .s-j{color:var(--vac);font-weight:700}
.note{font-size:7.8pt;color:var(--ink-2);background:#f7f8fa;border-left:1.6pt solid var(--acc-line);
  padding:2.4mm 3mm;border-radius:0 1.2mm 1.2mm 0;line-height:1.5}
.note b{color:var(--ink)}
.ft{margin-top:auto;padding-top:3mm;border-top:.6pt solid var(--rule);
  display:flex;justify-content:space-between;font-size:6.4pt;color:var(--ink-3)}
@page{size:A4;margin:0}
"""

HTML = f"""<meta charset="utf-8">
<title>Calendrier des cours 2026-2027</title>
<style>{CSS}</style>

<div class="page">
  <div class="hd">
    <div>
      <div class="hd-eyebrow">Année scolaire 2026 — 2027</div>
      <h1>Calendrier des cours</h1>
      <div class="hd-sub">Du <b>{fr_jour(start)}</b> au <b>{fr_jour(end)}</b>
        &nbsp;·&nbsp; cours du lundi au samedi</div>
    </div>
    <div class="hd-r"><div class="hd-big">168</div><div class="hd-lab">jours de cours</div></div>
  </div>

  <div class="stats">
    <div class="st"><div class="st-v">28 semaines</div>
      <div class="st-l">de cours réparties sur 10 mois</div></div>
    <div class="st"><div class="st-v">6 jours / semaine</div>
      <div class="st-l">lundi &rarr; samedi, jamais le dimanche</div></div>
    <div class="st"><div class="st-v">28 × chaque jour</div>
      <div class="st-l">28 lundis, 28 mardis… 28 samedis</div></div>
    <div class="st"><div class="st-v">5 interruptions</div>
      <div class="st-l">de deux semaines chacune</div></div>
  </div>

  <div class="lg">
    <span><i class="k-c"></i>Jour de cours</span>
    <span><i class="k-v"></i>Interruption</span>
    <span><i class="k-d"></i>Dimanche</span>
    <span><i class="k-j"></i>Rentrée &amp; dernier jour</span>
  </div>

  <div class="mois">{vignettes}{carte_vac}</div>
</div>

<div class="page">
  <div class="hd">
    <div>
      <div class="hd-eyebrow">Repères</div>
      <h1>Le rythme de l’année</h1>
      <div class="hd-sub">Six périodes de cours séparées par cinq interruptions</div>
    </div>
    <div class="hd-r"><div class="hd-big">6</div><div class="hd-lab">périodes</div></div>
  </div>

  <div class="sec">
    <div class="rythme">{alt}</div>
  </div>

  <div class="sec">
    <div class="h2">Semaine par semaine</div>
    <div class="h2-s">Chaque semaine compte six jours de cours, du lundi au samedi.</div>
    <ul class="sems">{lignes_sem}</ul>
  </div>

  <div class="note">
    <b>Deux semaines particulières.</b> La semaine 03 s’arrête le vendredi 16 octobre
    (l’interruption de la Toussaint commence le samedi), et la semaine 04 ne compte que le
    samedi 31 octobre, jour de reprise. Ensemble, elles forment bien six jours de cours&nbsp;:
    l’année totalise ainsi 28 séances pour chaque jour de la semaine.
  </div>

  <div class="ft">
    <span>Calendrier des cours · année scolaire 2026 — 2027</span>
    <span>{fr(start)} &rarr; {fr(end)} · 168 jours</span>
  </div>
</div>
"""

out = pathlib.Path("/home/user/claude/calendrier/calendrier-cours-2026-2027.html")
out.write_text(HTML, encoding="utf-8")
print("écrit:", out, len(HTML), "octets")
