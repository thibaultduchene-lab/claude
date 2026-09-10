# -*- coding: utf-8 -*-
"""Génère Bilan_2025_MTCB.xlsx en reprenant la mise en forme du fichier 2024.

Différences voulues par rapport à 2024 : la colonne « Preuve de paiement » est
supprimée et la colonne « Facture » est laissée vide (à cocher à la main).
"""
import sys, copy
import openpyxl
from openpyxl.styles import Alignment
from data_2025 import MOIS

TPL = '/root/.claude/uploads/a796c884-0d6f-5120-8cad-e2cfd2d80b96/f5e00871-Bilan_2024_MTCB.xlsx'
OUT = sys.argv[1] if len(sys.argv) > 1 else 'Bilan_2025_MTCB.xlsx'
COLS = 'EFGHIJK'               # K = Remarque, une fois « Preuve de paiement » retirée
BLANK_AFTER_MONTH = 2          # comme en 2024 : 2 lignes vides entre les mois
LARGEUR_MAX = 60               # largeur max de la colonne Remarque

wb = openpyxl.load_workbook(TPL)
ws = wb['Feuil1']

# 1. supprimer la colonne « Preuve de paiement » (K) : « Remarque » (L) devient K
largeur_remarque = ws.column_dimensions['L'].width
ws.delete_cols(11)
ws.column_dimensions['K'].width = largeur_remarque
del ws.column_dimensions['L']

# 2. mémoriser les styles du modèle avant de vider la feuille
sty_first = {c: copy.copy(ws[f'{c}31']._style) for c in COLS}   # 1re ligne d'un mois
sty_row   = {c: copy.copy(ws[f'{c}7']._style)  for c in COLS}   # ligne courante
sty_total = {c: copy.copy(ws[f'{c}310']._style) for c in COLS}  # ligne de total

# 3. vider les anciennes données (lignes 6 à 310), garder les en-têtes 4 et 5
ws.delete_rows(6, 305)
ws['D4'] = 'Déclaration MT Cosmetics Belgium 2025'

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
        if k < len(m['depenses']):
            src, mnt, rem = m['depenses'][k]
            ws[f'H{r+k}'], ws[f'I{r+k}'] = src, mnt
            if rem:
                ws[f'K{r+k}'] = rem
    r += n + BLANK_AFTER_MONTH

# 5. ligne de totaux (comme G310/I310 en 2024)
last = r - BLANK_AFTER_MONTH - 1
for c in COLS:
    ws[f'{c}{r}']._style = copy.copy(sty_total[c])
ws[f'G{r}'] = f'=SUM(G{first_data_row}:G{last})'
ws[f'I{r}'] = f'=SUM(I{first_data_row}:I{last})'

for c in 'GI':
    for row in range(first_data_row, r + 1):
        ws[f'{c}{row}'].number_format = '#,##0.00'

for idx in [i for i in ws.row_dimensions if i > r]:   # hauteurs résiduelles du modèle
    del ws.row_dimensions[idx]

# 6. colonne Remarque : assez large pour le texte, avec retour à la ligne
#    au-delà de LARGEUR_MAX pour ne pas déformer la feuille
longueur = max([len(str(ws[f'K{row}'].value)) for row in range(5, r + 1)
                if ws[f'K{row}'].value] or [0])
ws.column_dimensions['K'].width = min(longueur + 3, LARGEUR_MAX)
for row in range(first_data_row, r + 1):
    ws[f'K{row}'].alignment = Alignment(wrap_text=True, vertical='top')

wb.save(OUT)
print(f'{OUT} écrit — données lignes {first_data_row} à {last}, totaux ligne {r}')
