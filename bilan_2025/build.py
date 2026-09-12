# -*- coding: utf-8 -*-
"""Génère Bilan_2025_MTCB.xlsx en reprenant la mise en forme du fichier 2024.

Différences voulues par rapport à 2024 :
  - la colonne « Preuve de paiement » est supprimée ;
  - la colonne « Facture » est laissée vide (à cocher à la main) ;
  - les entrées ont leur propre colonne Remarque (en 2024 elle était partagée
    avec les dépenses, donc inutilisable dès qu'il y avait les deux) ;
  - les lignes qui demandent un arbitrage sont surlignées en jaune.

Colonnes : E Mois | F G H Entrées (Source, Montant, Remarque)
                  | I J K L Dépenses (Source, Montant, Facture, Remarque)
"""
import re
import sys
import copy
import importlib
import openpyxl
from openpyxl.styles import Alignment, PatternFill
ANNEE = sys.argv[1] if len(sys.argv) > 1 else '2025'
OUT = sys.argv[2] if len(sys.argv) > 2 else f'Bilan_{ANNEE}_MTCB.xlsx'
TPL = '/root/.claude/uploads/a796c884-0d6f-5120-8cad-e2cfd2d80b96/f5e00871-Bilan_2024_MTCB.xlsx'


def charger(module, defauts):
    """Décomptes de carte et justificatifs : absents d'une année qu'on ouvre."""
    try:
        m = importlib.import_module(module)
    except ModuleNotFoundError:
        return [val for _, val in defauts]
    return [getattr(m, nom, val) for nom, val in defauts]


MOIS = importlib.import_module(f'data_{ANNEE}').MOIS
DECOMPTES, DECOMPTES_MC = charger(f'cartes_{ANNEE}',
                                  [('DECOMPTES', {}), ('DECOMPTES_MC', {})])
JUSTIFICATIFS, SANS_TICKET = charger(f'justificatifs_{ANNEE}',
                                     [('JUSTIFICATIFS', []), ('SANS_TICKET', [])])
COLS = 'EFGHIJKL'
BLANK_AFTER_MONTH = 2          # comme en 2024 : 2 lignes vides entre les mois
LARGEUR_MAX = 60               # largeur max des colonnes Remarque
LARGEURS = {'E': 10.29, 'F': 32.29, 'G': 9.0, 'I': 47.29, 'J': 8.43, 'K': 7.71}
JAUNE = PatternFill('solid', fgColor='FFFF00')    # il manque une pièce
ORANGE = PatternFill('solid', fgColor='FFC000')   # arbitrage à trancher

# Postes pour lesquels le comptable ne demande pas de justificatif : la colonne
# Facture reçoit un X, comme en 2024. Carburant, parkings, transports en commun,
# crédit voiture et impôts.
SANS_FACTURE = {'Carburant', 'Crédit voiture', 'Versement impôts anticipé',
                'Impôt des sociétés', 'Précompte mobilier',
                'Vlaamse Belastingsdienst - taxe de circulation'}
PREFIXES_SANS_FACTURE = ('Parking', 'Transport')

# Avances privées payées par la société et remboursées en entier par le gérant
# quelques jours plus tard : la dépense et l'entrée s'annulent, il n'y a pas de
# charge à justifier. L'extrait bancaire suffit à prouver le remboursement.
SANS_FACTURE |= {"Billet d'avion Lima-Bruxelles - Air Europa",
                 'Séjour Sandaya Lyon'}


def sans_facture(libelle):
    return libelle in SANS_FACTURE or str(libelle).startswith(PREFIXES_SANS_FACTURE)

# une remarque contenant un de ces marqueurs = point à trancher avec le comptable
# lignes que Thibault veut garder en jaune même si la remarque ne le dit pas
FORCER_JAUNE = {"Billets d'avion Pérou - Translatina Travel"}

A_TRANCHER = re.compile(
    r"à (confirmer|identifier|préciser|vérifier|valider|joindre|traiter|trancher|amortir)"
    r"|sans numéro|privée|compte courant|documenter|\?", re.I)


def eclater_cartes(mois, decomptes, ligne_globale, carte):
    """Remplace la ligne globale de paiement de carte par le détail du décompte."""
    for nom, m in mois:
        if nom not in decomptes:
            continue
        num, prel, lignes = decomptes[nom]
        detail = [(lib, mnt,
                   f"Carte {carte} {dt} — décompte n° {num} du {prel}" + (f" — {rem}" if rem else ""))
                  for dt, lib, mnt, rem in lignes]
        dep = []
        for d in m['depenses']:
            dep.extend(detail if d[0] == ligne_globale else [d])
        m['depenses'] = dep


eclater_cartes(MOIS, DECOMPTES, 'Paiement carte VISA', 'Visa')
eclater_cartes(MOIS, DECOMPTES_MC, 'Paiement carte MASTERCARD', 'Mastercard')

wb = openpyxl.load_workbook(TPL)
ws = wb['Feuil1']

# 1. colonnes : retirer « Preuve de paiement », ajouter une Remarque pour les entrées
ws.delete_cols(11)             # ancienne colonne K
ws.insert_cols(8)              # nouvelle colonne H, avant les dépenses

# 2. mémoriser les styles du modèle avant de vider la feuille
sty_first = {c: copy.copy(ws[f'{c}31']._style) for c in COLS}   # 1re ligne d'un mois
sty_row = {c: copy.copy(ws[f'{c}7']._style) for c in COLS}      # ligne courante
sty_total = {c: copy.copy(ws[f'{c}310']._style) for c in COLS}  # ligne de total
for sty in (sty_first, sty_row, sty_total):                     # la colonne ajoutée
    sty['H'] = copy.copy(sty['L'])                              # se cale sur Remarque

ws['H4']._style = copy.copy(ws['G4']._style)
ws['H5']._style = copy.copy(ws['G5']._style)
ws['H5'] = 'Remarque'

# 3. vider les anciennes données (lignes 6 à 310), garder les en-têtes 4 et 5
ws.delete_rows(6, 305)
ws['D4'] = f'Déclaration MT Cosmetics Belgium {ANNEE}'

# 4. réécrire les blocs mensuels
r = 6
first_data_row = r
for i, (nom, m) in enumerate(MOIS):
    n = max(len(m['entrees']), len(m['depenses']))
    for k in range(n):
        sty = sty_first if k == 0 and i > 0 else sty_row
        for c in COLS:
            ws[f'{c}{r+k}']._style = copy.copy(sty[c])
        if k == 0:
            ws[f'E{r}'] = nom
        if k < len(m['entrees']):
            src, mnt, rem = m['entrees'][k]
            ws[f'F{r+k}'], ws[f'G{r+k}'] = src, mnt
            if rem:
                ws[f'H{r+k}'] = rem
        if k < len(m['depenses']):
            src, mnt, rem = m['depenses'][k]
            ws[f'I{r+k}'], ws[f'J{r+k}'] = src, mnt
            if rem:
                ws[f'L{r+k}'] = rem
    r += n + BLANK_AFTER_MONTH

# 5. ligne de totaux (comme G310/I310 en 2024)
last = r - BLANK_AFTER_MONTH - 1
for c in COLS:
    ws[f'{c}{r}']._style = copy.copy(sty_total[c])
ws[f'G{r}'] = f'=SUM(G{first_data_row}:G{r-1})'   # jusqu'aux lignes vides,
ws[f'J{r}'] = f'=SUM(J{first_data_row}:J{r-1})'   # pour englober un ajout en bas

for c in 'GJ':
    for row in range(first_data_row, r + 1):
        ws[f'{c}{row}'].number_format = '#,##0.00'

for col, largeur in LARGEURS.items():
    ws.column_dimensions[col].width = largeur
for col in 'HL':               # les deux colonnes Remarque, avec retour à la ligne
    longueur = max([len(str(ws[f'{col}{row}'].value)) for row in range(5, r + 1)
                    if ws[f'{col}{row}'].value] or [0])
    ws.column_dimensions[col].width = min(longueur + 3, LARGEUR_MAX)
    for row in range(first_data_row, r + 1):
        ws[f'{col}{row}'].alignment = Alignment(wrap_text=True, vertical='top')

for idx in [i for i in ws.row_dimensions if i > r]:   # hauteurs résiduelles du modèle
    del ws.row_dimensions[idx]

# 7. colonne Facture : V sur les lignes dont le justificatif est en main
attendus = {(mois, lib, round(mnt, 2)): pdf for mois, lib, mnt, pdf in JUSTIFICATIFS}
trouves = set()
mois_courant = ''
for row in range(first_data_row, r):
    if ws[f'E{row}'].value:
        mois_courant = ws[f'E{row}'].value
    cle = (mois_courant, ws[f'I{row}'].value, round(ws[f'J{row}'].value or 0, 2))
    if cle not in attendus:
        continue
    ws[f'K{row}'] = 'V'
    piece = attendus[cle]
    note = f"Justificatif : {piece}" if piece.endswith('.pdf') else piece
    ws[f'L{row}'] = f"{ws[f'L{row}'].value} — {note}" if ws[f'L{row}'].value else note
    trouves.add(cle)
manquants = set(attendus) - trouves
if manquants:
    raise SystemExit(f'justificatif sans ligne correspondante : {manquants}')

# Tickets perdus : un X, mais accompagné d'une remarque et d'un surlignage —
# sans quoi il se confondrait avec les postes que le comptable dispense de
# justificatif, ce qui laisserait croire la question réglée.
PERDU = "Ticket non conservé — pièce manquante"
perdus = {(m, lib, round(mnt, 2)) for m, lib, mnt in SANS_TICKET}
vus = set()
n_perdus = 0
mois_courant = ''
for row in range(first_data_row, r):
    if ws[f'E{row}'].value:
        mois_courant = ws[f'E{row}'].value
    cle = (mois_courant, ws[f'I{row}'].value, round(ws[f'J{row}'].value or 0, 2))
    if cle not in perdus or ws[f'K{row}'].value:
        continue
    ws[f'K{row}'] = 'X'
    ancienne = ws[f'L{row}'].value
    ws[f'L{row}'] = f'{ancienne} — {PERDU}' if ancienne else PERDU
    vus.add(cle)
    n_perdus += 1
if perdus - vus:
    raise SystemExit(f'ticket perdu sans ligne correspondante : {perdus - vus}')

n_x = n_perdus
for row in range(first_data_row, r):
    if sans_facture(ws[f'I{row}'].value) and not ws[f'K{row}'].value:
        ws[f'K{row}'] = 'X'
        n_x += 1

# 8. couleurs : jaune quand une pièce manque, orange quand il faut trancher.
# Une ligne peut être les deux ; l'orange l'emporte, parce que la pièce
# manquante se voit déjà à la colonne Facture restée vide.
def arbitrage(rem, source):
    return bool(rem and A_TRANCHER.search(str(rem))) or source in FORCER_JAUNE

n_orange = n_manque = 0
for row in range(first_data_row, r):
    # entrées : pas de colonne Facture, donc seul l'arbitrage les concerne
    if arbitrage(ws[f'H{row}'].value, ws[f'F{row}'].value):
        for c in 'FGH':
            ws[f'{c}{row}'].fill = ORANGE
        n_orange += 1
    if not ws[f'I{row}'].value:
        continue
    manque = not ws[f'K{row}'].value or ws[f'K{row}'].value == 'X' and PERDU in str(ws[f'L{row}'].value)
    if arbitrage(ws[f'L{row}'].value, ws[f'I{row}'].value):
        couleur, n_orange = ORANGE, n_orange + 1
    elif manque:
        couleur, n_manque = JAUNE, n_manque + 1
    else:
        continue
    for c in 'IJKL':
        ws[f'{c}{row}'].fill = couleur

ws['D5'] = ('Jaune = pièce manquante  ·  Orange = à trancher avec le comptable')

wb.save(OUT)
print(f'{OUT} écrit — lignes {first_data_row} à {last}, totaux ligne {r}, '
      f'{n_manque} pièce(s) manquante(s) en jaune, '
      f'{n_orange} arbitrage(s) en orange, '
      f'{len(trouves)} justificatif(s) rattaché(s), '
      f'{n_perdus} ticket(s) perdu(s)')
