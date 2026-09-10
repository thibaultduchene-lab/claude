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


def recadrer(img, seuil=0.55, marge=40):
    """Découpe la zone claire (le ticket) du fond."""
    gris = np.asarray(ImageOps.grayscale(img), dtype=float) / 255.0
    masque = gris > seuil
    lignes, colonnes = masque.sum(axis=1), masque.sum(axis=0)
    if not masque.any():
        return img
    y = np.where(lignes > lignes.max() * 0.12)[0]
    x = np.where(colonnes > colonnes.max() * 0.12)[0]
    box = (max(int(x[0]) - marge, 0), max(int(y[0]) - marge, 0),
           min(int(x[-1]) + marge, img.width), min(int(y[-1]) + marge, img.height))
    return img.crop(box)


def masque_ticket(img, seuil=0.55):
    """Masque booléen du ticket (zone claire) dans l'image."""
    return np.asarray(ImageOps.grayscale(img), dtype=float) / 255.0 > seuil


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
    page = en_a4(nettoyer(recadrer(redresser(recadrer(photo)))))
    page.save(dst, 'PDF', resolution=300.0)
    print(f'{dst} écrit ({page.size[0]}x{page.size[1]} px, A4 300 dpi)')
