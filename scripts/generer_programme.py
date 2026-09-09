# -*- coding: utf-8 -*-
"""Genere les documents Word "Programme <joueur>" de l'ecole de tennis du Lambermont.

Le logo est place en haut du corps du document (et non dans la zone d'en-tete
de Word, qui s'affiche en grise tant qu'on edite le corps du document).
"""
import sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

LOGO = "/home/user/claude/assets/logo_lambermont.png"

PROGRAMMES = {
    "Petra_NAGY": {
        "titre": "Programme Petra NAGY",
        "planning": [
            "Lundi : Privé 16h – 17h (Yassine)",
            "Mercredi : Collectif 14h – 15h (Yassine)",
            "Vendredi : Privé 16h – 17h (Yassine)",
            "Samedi : Physique sur terrain 10h – 11h et Collectif 11h – 12h (avec Adel)",
        ],
        "note": "Les cours privés (lundi et vendredi) sont à payer directement à Yassine.",
        "tableau": [
            ("2h de terrains (privés)", "1050", "Gratuit"),
            ("1h de physique", "………", "Gratuit"),
            ("Collectif 2h", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Djena": {
        "titre": "Programme Djena",
        "planning": [
            "Mercredi : Physique 14h – 15h30 (avec Loïc) et Privé 17h30 – 18h30 (Yassine)",
            "Jeudi : Collectif 17h30 – 19h (avec Taha)",
            "Samedi : Physique sur terrain 11h – 12h et League Cup 15h – 16h30",
        ],
        "note": "Le cours privé (mercredi) est à payer directement à Yassine.",
        "tableau": [
            ("1h de terrain (privé)", "525", "Gratuit"),
            ("1h30 de physique", "………", "………"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 1h30", "………", "………"),
            ("League Cup", "250", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Noah_Vicente": {
        "titre": "Programme Noah Vicente",
        "planning": [
            "Lundi : Privé 16h – 17h (Thibault)",
            "Mercredi : Semi-privé 13h30 – 14h30 avec Samuel (Thibault)",
            "Jeudi : Collectif 16h30 – 17h30 (avec Taha)",
            "Samedi : Rassemblement 13h30 – 15h",
        ],
        "note": "Le cours privé (lundi) et le semi-privé (mercredi) sont à payer directement à Thibault.",
        "tableau": [
            ("1h de terrain (privé)", "525", "Gratuit"),
            ("1h de semi-privé", "………", "………"),
            ("Collectif 1h", "………", "………"),
            ("Rassemblement 1h30", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Aleksander_LUKACHI": {
        "titre": "Programme Aleksander LUKACHI",
        "planning": [
            "Lundi : Physique 16h45 – 18h15 (avec Loïc)",
            "Mardi : Privé 16h30 – 17h30 (Yassine)",
            "Mercredi : Collectif 16h – 17h30 (avec Julien)",
            "Jeudi : Collectif 17h – 18h30 (avec Yassine)",
            "Samedi : Physique sur terrain 10h – 11h et League Cup 15h – 16h30",
        ],
        "note": "Le cours privé (mardi) est à payer directement à Yassine.",
        "tableau": [
            ("1h de terrain (privé)", "525", "Gratuit"),
            ("1h30 de physique", "………", "………"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 3h", "………", "………"),
            ("League Cup", "250", "………"),
            ("Total", "………", "………"),
        ],
    },
}


def filet_bas(par, sz, couleur):
    """Filet sous le paragraphe, insere a la position imposee par le schema OOXML."""
    pPr = par._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(sz))
    bottom.set(qn("w:space"), "4")
    bottom.set(qn("w:color"), couleur)
    bdr.append(bottom)
    style = pPr.find(qn("w:pStyle"))
    if style is not None:
        style.addnext(bdr)
    else:
        pPr.insert(0, bdr)


def generer(cle, data, dossier="/home/user/claude"):
    doc = Document()

    sec = doc.sections[0]
    sec.top_margin = Cm(1.5)
    sec.bottom_margin = Cm(2)
    sec.left_margin = Cm(2.5)
    sec.right_margin = Cm(2.5)

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(11)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    normal.paragraph_format.space_after = Pt(10)

    # En-tete dans le corps du document : logo + nom de l'ecole + filet
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_after = Pt(2)
    p_logo.add_run().add_picture(LOGO, width=Cm(8))

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(4)
    r = p_sub.add_run("École de tennis du Lambermont")
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x26, 0x26, 0x26)
    r.bold = True
    filet_bas(p_sub, 12, "55621E")

    # Titre
    titre = doc.add_paragraph()
    tr = titre.add_run(data["titre"])
    tr.bold = True
    tr.font.size = Pt(14)
    titre.paragraph_format.space_before = Pt(18)
    titre.paragraph_format.space_after = Pt(14)
    filet_bas(titre, 6, "000000")

    # Planning
    for ligne in data["planning"]:
        doc.add_paragraph(ligne)

    if data.get("note"):
        note = doc.add_paragraph()
        nr = note.add_run(data["note"])
        nr.italic = True
        note.paragraph_format.space_before = Pt(6)
        note.paragraph_format.space_after = Pt(14)
    else:
        doc.paragraphs[-1].paragraph_format.space_after = Pt(20)

    # Tableau
    lignes = [("Cours", "Prix normal (€)", "Prix adapté (€)")] + list(data["tableau"])
    table = doc.add_table(rows=len(lignes), cols=3)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    largeurs = [Cm(6.5), Cm(4.0), Cm(5.5)]
    for i, ligne in enumerate(lignes):
        cells = table.rows[i].cells
        for j, txt in enumerate(ligne):
            cells[j].width = largeurs[j]
            para = cells[j].paragraphs[0]
            para.paragraph_format.space_before = Pt(2)
            para.paragraph_format.space_after = Pt(2)
            run = para.add_run(txt)
            if i == 0 or i == len(lignes) - 1:
                run.bold = True

    zoom = doc.settings.element.find(qn("w:zoom"))
    if zoom is not None and zoom.get(qn("w:percent")) is None:
        zoom.set(qn("w:percent"), "100")

    chemin = "%s/Programme_%s.docx" % (dossier, cle)
    doc.save(chemin)
    return chemin


if __name__ == "__main__":
    cles = sys.argv[1:] or list(PROGRAMMES)
    for cle in cles:
        print(generer(cle, PROGRAMMES[cle]))
