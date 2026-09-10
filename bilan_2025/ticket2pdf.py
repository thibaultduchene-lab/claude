# -*- coding: utf-8 -*-
"""Transforme la photo d'un ticket en PDF A4 propre, prêt pour Billtobox.

Recadre le ticket (zone claire sur fond sombre), redresse légèrement, relève le
contraste, puis pose l'image sur une page A4 blanche avec une marge.

    python3 ticket2pdf.py photo.jpg sortie.pdf
"""
import sys
import numpy as np
from PIL import Image, ImageOps, ImageEnhance

A4 = (2480, 3508)      # A4 à 300 dpi
MARGE = 120            # marge blanche autour du ticket, en pixels


def recadrer(img, marge=40):
    """Découpe le ticket (zone claire) du fond.

    On prend la boîte qui contient 99 % des pixels clairs — insensible aux
    reflets isolés du fond — et on repasse à la boîte complète si ce cadrage
    perdait une partie du ticket. Rogner trop est bien pire que pas assez :
    un ticket amputé ne vaut plus rien comme justificatif.
    """
    m = masque_ticket(img)
    if not m.any():
        return img
    ys, xs = np.where(m)
    boite = [int(np.quantile(xs, 0.005)), int(np.quantile(ys, 0.005)),
             int(np.quantile(xs, 0.995)), int(np.quantile(ys, 0.995))]
    garde = m[boite[1]:boite[3] + 1, boite[0]:boite[2] + 1].sum() / m.sum()
    if garde < 0.92:                            # cadrage trop serré
        boite = [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]
    if (boite[2] - boite[0]) < img.width * 0.05 or (boite[3] - boite[1]) < img.height * 0.05:
        return img
    return img.crop((max(boite[0] - marge, 0), max(boite[1] - marge, 0),
                     min(boite[2] + marge, img.width), min(boite[3] + marge, img.height)))


def seuil_otsu(gris):
    """Seuil de séparation fond / ticket, calculé sur l'histogramme (Otsu)."""
    hist, _ = np.histogram(gris, bins=256, range=(0, 1))
    p = hist / hist.sum()
    omega = np.cumsum(p)
    mu = np.cumsum(p * np.arange(256))
    with np.errstate(invalid='ignore', divide='ignore'):
        variance = (mu[-1] * omega - mu) ** 2 / (omega * (1 - omega))
    return int(np.nanargmax(variance)) / 255.0


def masque_ticket(img, seuil=None):
    """Masque booléen du ticket (zone claire) dans l'image."""
    gris = np.asarray(ImageOps.grayscale(img), dtype=float) / 255.0
    if seuil is None:
        seuil = max(seuil_otsu(gris), 0.72)
    return gris > seuil


def masque_fiable(img):
    """Le découpage n'a de sens que si le ticket se détache vraiment du fond.
    Sur un fond clair (table en bois, mur blanc) ce n'est pas le cas : on laisse
    alors la photo entière plutôt que de découper n'importe où."""
    part = masque_ticket(img).mean()
    return 0.03 < part < 0.85


def redresser(img, amplitude=12):
    """Redresse le ticket : l'angle retenu est celui qui donne le plus petit
    rectangle englobant, donc celui où le ticket est le plus droit."""
    meilleur, angle_retenu = None, 0
    for angle in range(-amplitude, amplitude + 1):
        m = masque_ticket(img.rotate(angle, expand=True, fillcolor='black'))
        if not m.any():
            continue
        ys, xs = np.where(m)
        aire = (ys.max() - ys.min()) * (xs.max() - xs.min())
        if meilleur is None or aire < meilleur:
            meilleur, angle_retenu = aire, angle
    return img.rotate(angle_retenu, expand=True, fillcolor='black', resample=Image.BICUBIC)


def blanchir_fond(img, seuil=0.35):
    """Remplace le fond sombre autour du ticket par du blanc.

    Le bord du ticket est souvent dans l'ombre : on prend un seuil bas, puis on
    lisse les bords gauche et droit sur une fenêtre glissante, sinon la découpe
    fait des marches d'escalier dans la zone ombrée.
    """
    m = masque_ticket(img, seuil)
    h = m.shape[0]
    gauche = np.full(h, -1)
    droite = np.full(h, -1)
    for i, ligne in enumerate(m):
        cols = np.where(ligne)[0]
        if cols.size >= 20:
            gauche[i], droite[i] = cols[0], cols[-1]

    fen = max(h // 20, 5)                       # fenêtre de lissage
    plein = np.where(gauche >= 0)[0]
    a = np.asarray(ImageOps.grayscale(img)).copy()
    if plein.size == 0:
        return Image.fromarray(a)
    haut, bas = plein[0], plein[-1]
    for i in range(h):
        if not (haut <= i <= bas):
            a[i, :] = 255
            continue
        vois = slice(max(i - fen, 0), min(i + fen + 1, h))
        g = gauche[vois][gauche[vois] >= 0]
        d = droite[vois][droite[vois] >= 0]
        if g.size == 0:
            continue
        a[i, :int(g.min())] = 255
        a[i, int(d.max()) + 1:] = 255
    return Image.fromarray(a)


def nettoyer(img):
    """Rend le ticket lisible : gris, fond blanchi, contraste relevé."""
    img = blanchir_fond(img)
    img = ImageOps.autocontrast(img, cutoff=(1, 12))
    return ImageEnhance.Contrast(img).enhance(1.35)


def en_colonnes(img, gouttiere=60):
    """Un ticket très allongé tient mal sur une page A4 : on le coupe en
    colonnes posées côte à côte, ce qui agrandit d'autant le texte."""
    ratio = img.height / img.width
    n = max(1, min(4, round((ratio / (A4[1] / A4[0])) ** 0.5)))
    if n == 1:
        return img
    recouvrement = img.height // 120           # évite de couper une ligne net
    hauteur = img.height // n
    morceaux = []
    for i in range(n):
        haut = max(0, i * hauteur - recouvrement)
        bas = min(img.height, (i + 1) * hauteur + recouvrement)
        morceaux.append(img.crop((0, haut, img.width, bas)))
    largeur = sum(m.width for m in morceaux) + gouttiere * (n - 1)
    page = Image.new('L', (largeur, max(m.height for m in morceaux)), 255)
    x = 0
    for m in morceaux:
        page.paste(m, (x, 0))
        x += m.width + gouttiere
    return page


def en_a4(img):
    page = Image.new('RGB', A4, 'white')
    dispo = (A4[0] - 2 * MARGE, A4[1] - 2 * MARGE)
    ratio = min(dispo[0] / img.width, dispo[1] / img.height)
    img = img.resize((int(img.width * ratio), int(img.height * ratio)), Image.LANCZOS)
    page.paste(img, ((A4[0] - img.width) // 2, (A4[1] - img.height) // 2))
    return page


if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    photo = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    if masque_fiable(photo):
        page = en_a4(en_colonnes(nettoyer(recadrer(redresser(recadrer(photo))))))
    else:                                   # fond clair : on garde la photo telle quelle
        gris = ImageOps.autocontrast(ImageOps.grayscale(photo), cutoff=(1, 8))
        page = en_a4(ImageEnhance.Contrast(gris).enhance(1.25))
    page.save(dst, 'PDF', resolution=300.0)
    print(f'{dst} écrit ({page.size[0]}x{page.size[1]} px, A4 300 dpi)')
