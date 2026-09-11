# -*- coding: utf-8 -*-
# Données 2026 — bilan provisoire, repris des extraits BNP Paribas Fortis
# BE23 0019 5419 0591 — BV MT COSMETICS BELGIUM
#
# Même convention qu'en 2025 : les charges de décembre 2025 débitées début
# janvier 2026 (précompte salarial 2.250,00 et SD Worx 331,85) sont comptées
# dans le bilan 2025 et donc EXCLUES ici. L'extrait 2026-001 ne se rapproche
# pas du solde pour cette raison : écart voulu de 2.581,85.

MOIS = []

MOIS.append(("Janvier", {
 "solde_debut": 8522.89, "solde_fin": 1378.82, "extrait": "2026 - 001",
 "entrees": [],   # aucun encaissement du mois
 "depenses": [
    ("Carburant",                                         69.70, "Shell Kraainem"),
    ("Achat matériel sportif - DECATHLON",                240.00, "Decathlon Evere"),
    ("Achat matériel sportif - DECATHLON",                108.50, "Decathlon Evere"),
    ("Parking",                                           4.80, "Woluwe-Saint-Lambert"),
    ("Crédit voiture",                                    724.12, ""),
    ("Entretien voiture - Auto 5 Kraainem",               1094.40, ""),
    ("Entretien voiture - Auto 5 Kraainem",               70.00, ""),
    ("Carburant",                                         44.88, "Lukoil Wezembeek"),
    ("Carburant",                                         65.20, "Total Saverne (France)"),
    ("Frais bancaires trimestriels",                      11.25, ""),
    ("Carburant",                                         57.46, "BP Vaduz (Liechtenstein) — 51,90 CHF"),
    ("Parking",                                           20.30, "Parkhaus Bahnhofplatz, Coire (Suisse) — 18,00 CHF"),
    ("Carburant",                                         73.48, "Esso Brumath (France)"),
    ("Parking",                                           1.85, "Q-Park Woluwe Esplanade"),
    ("Carburant",                                         74.63, "Q8 Easy Zaventem"),
    ("Assurance voiture",                                 458.66, "Domiciliation AG Insurance"),
    ("Proximus",                                          184.72, ""),
    ("Parking",                                           11.00, "Parking Grand-Place, Bruxelles"),
    ("Carburant",                                         64.57, "Shell Kraainem"),
    ("Frais comptable BDH",                               1179.75, "Facture 20250542 — facture 2025 payée en 2026"),
    ("Parking",                                           1.60, "Woluwe-Saint-Lambert"),
    ("Parking",                                           1.35, "Schaerbeek"),
 ],
}))
