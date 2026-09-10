# -*- coding: utf-8 -*-
"""Tickets et factures reçus, rattachés à leur ligne du bilan.

Une entrée = (mois, libellé exact de la dépense, montant, nom du PDF).
La colonne « Facture » passe à V et le nom du justificatif est ajouté en
remarque. Les PDF sont dans ../justificatifs_2025/.
"""

JUSTIFICATIFS = [
    ("Janvier", "Repas Topogigio", 22.00, "2025-01-10_RTCL-Lambermont_22.00.pdf"),
]
