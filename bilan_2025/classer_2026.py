# -*- coding: utf-8 -*-
"""Relit les extraits 2026 et propose une classification des opérations.
Ce qui n'est pas reconnu est listé pour être traité à la main."""
import re, glob
from pypdf import PdfReader

FICH = {'02':'de723efb','03':'4c312ca8','04':'d8ce7a54','05':'7e3b8bad',
        '06':'bdc6539c','07':'3a58206d','08':'904c7f0b'}
DOSSIER = '/root/.claude/uploads/a796c884-0d6f-5120-8cad-e2cfd2d80b96/'

REGLES = [
 # commerçants rencontrés en 2026
 (r'DAVID LLOYD', ('Abonnement club David Lloyd', 'Sterrebeek — usage professionnel à confirmer')),
 (r'FITRAW', ('Abonnement salle FitRaw', 'Sterrebeek — usage professionnel à confirmer')),
 (r'SV Victoria', ('Consommation - SV Victoria', 'Rotterdam (Pays-Bas)')),
 (r'Nike ', ('Achat vêtements sport - NIKE', '')),
 (r'SPORTSDIRECT', ('Achat vêtements sport - Sportsdirect', '')),
 (r'NEW BS SPRL', ('Achat matériel sportif - Bellissimo Sport', '')),
 (r'Monsieur Pneus', ('Entretien voiture - Monsieur Pneus', '')),
 (r'Wash Time', ('Lavage voiture', 'Wash Time Tervuren')),
 (r'YUZZU', ('Assurance voiture - Yuzzu', '')),
 (r'FOD/SPF FIN', ('Versement impôts anticipé', 'Comm. 073/4616/33527')),
 (r'UNITED PARCEL', ('Réception marchandise - UPS', '')),
 (r'Optimal Parking|OPC BLANKENBERGE', ('Redevance de stationnement - OPC',
                                        'à confirmer (redevance ou amende)')),
 (r'CHIREC', ('Parking - Chirec', 'Hôpital, Bruxelles — à confirmer')),
 (r'BERCA', ('Achat - Berca', 'Ardooie — à identifier')),
 (r'ORGEFI', ('Achat - Orgefi SPRL', 'Nivelles — à identifier')),
 (r'IBIS STYLES', ('Hôtel Ibis Nieuwpoort', 'à confirmer (nuitée ou consommation)')),
 (r'CASTILLON FREJUS', ('Achat - Castillon Fréjus', 'France — à identifier')),
 (r'E\.LECLERC', ('Carburant', 'E.Leclerc Mornas (France) — à confirmer')),
 (r'MISTER MINIT', ('Divers - Mister Minit', '')),
 (r'BRASSERIE|Snack |ABATTOIR|BRABANT GARE', ('Collation', '')),
 (r'ES ROTSELAAR', ('Divers - sanitaires autoroute', 'Aire de Rotselaar')),
 (r'Sosta |Parcometro|GARAGE LA STAZIONE|COMUNE |ATC RIOMAGGIORE|GENOVA PIAZZA|TAP & GO',
  ('Parking', 'Italie')),
 (r'Q-PARK KOE|IDR NORD EINS', ('Parking', 'Düsseldorf (Allemagne)')),
 (r'Schiphol', ('Parking', 'Schiphol (Pays-Bas)')),
 (r'ASP PORT LACUSTR|SAINT TROPE|SAINT RAPHAEL|REGIE MUNICIP', ('Parking', 'Côte d\'Azur (France)')),
 (r'ADMINISTRATION COMMUNA', ('Parking', 'Administration communale, Bruxelles')),
 (r'ENI ?\d', ('Carburant', 'ENI (Italie)')),
 (r'TOTAL XB', ('Carburant', 'Total Schaerbeek')),
 (r'REMBOURSEMENT \d ALIMENTATION', ('Remboursement alimentation du compte - Thibault Duchène',
                                     'Restitution des apports de février 2026')),
 (r'Q8 |SHELL|ESSO|LUKOIL|TOTAL N|TOTAL PL|DATS|MAES |Station 15|TANKSTELLE|AVIA|BP ', 'Carburant'),
 (r'PARKING|Q PARK|PARKEREN|INDIGO|PARKHAUS|APCOA|INTERPARKING|MOBIB|PARKEER', 'Parking'),
 (r'Electrabel', 'Electrabel'), (r'Telenet', 'Telenet'), (r'PROXIMUS', 'Proximus'),
 (r'Farys', 'Farys (eau)'), (r'Partena', 'Partena'), (r'Xerius', 'Xerius'),
 (r'SD WORX', 'SD Worx'), (r'PRECOMPTE SALARIAL', 'Précompte salarial'),
 (r'Terugbetaling krediet', 'Crédit voiture'), (r'AG INSURANCE|AG Insurance', 'Assurance voiture'),
 (r'Trimestriële bijdrage', 'Frais bancaires trimestriels'),
 (r'Netto-intresten', 'Intérêt crédit'),
 (r'BDH CONSULT', 'Frais comptable BDH'), (r'FEDEX|FedEx', 'Réception marchandise - FEDEX'),
 (r'DECATHLON', 'Achat matériel sportif - DECATHLON'),
 (r'AUTOROUTES DU SUD|ASF', 'Péage autoroute France'),
 (r'Vlaamse Belasting', 'Vlaamse Belastingsdienst - taxe de circulation'),
 (r'Bank Card Company|Afrekening', 'Paiement carte de crédit'),
 (r'LAMBERMONT|RTCL', 'Consommation Lambermont'),
 (r'DE LIJN|DELIJN', 'Transport - De Lijn'), (r'STIB', 'Transport - STIB'),
 (r'LUNCH GARDEN', 'Repas Lunch Garden'), (r'EXKI|Exki', 'Repas Exki'),
 (r'Topogigio', 'Repas Topogigio'),
]

def lire(mois):
    txt = '\n'.join(p.extract_text(extraction_mode='layout')
                    for p in PdfReader(glob.glob(DOSSIER + FICH[mois] + '*.pdf')[0]).pages)
    txt = '\n'.join(re.sub(r'\s{2,}', ' | ', l.strip()) for l in txt.split('\n'))
    soldes = re.findall(r'saldo op (\d{2}-\d{2}-\d{4}) \| ([\d.]+,\d{2})', txt)
    debuts = [m.start() for m in re.finditer(r'^\d{4} \| ', txt, re.M)]
    ops = []
    for i, d in enumerate(debuts):
        bloc = txt[d:debuts[i+1] if i+1 < len(debuts) else len(txt)]
        t = re.match(r'^(\d{4}) \|(.*?)(\d{2}-\d{2}) \| ([\d.]+,\d{2})([-+])', bloc, re.S)
        if t:
            nr, tete, date, montant, signe = t.groups()
            ops.append((int(nr), date, signe,
                        float(montant.replace('.', '').replace(',', '.')),
                        re.sub(r'\s+', ' ', re.sub(r'\s*\|\s*', ' ', bloc[:420]))))
    fin = float(soldes[0][1].replace('.', '').replace(',', '.'))
    debut = float(soldes[1][1].replace('.', '').replace(',', '.'))
    return debut, fin, sorted(ops)

def classer(ctx):
    for motif, cible in REGLES:
        if re.search(motif, ctx):
            return cible if isinstance(cible, tuple) else (cible, '')
    return None
