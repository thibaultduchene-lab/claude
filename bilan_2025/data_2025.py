# -*- coding: utf-8 -*-
# Données 2025 — reprises des extraits de compte BNP Paribas Fortis
# BE23 0019 5419 0591 — BV MT COSMETICS BELGIUM
#
# Convention retenue : les opérations débitées/créditées début janvier 2025 mais
# se rapportant à décembre 2024 (et déjà encodées dans le bilan 2024) sont
# EXCLUES de 2025. Le total du mois ne correspond donc volontairement pas à la
# variation de solde de l'extrait bancaire.

MOIS = []

MOIS.append(("Janvier", {
 "solde_debut": 1378.02, "solde_fin": 3407.94, "extrait": "2025 - 001",
 # Exclus car déjà dans le bilan 2024 (décembre) :
 #   entrée  LAM2415 4.743,17
 #   dépenses Repas Topogigio 26,00 / Précompte salarial déc. 2024 2.250,00 /
 #            SD Worx 330,88 / Electrabel 256,99 / Telenet 149,10 / Proximus 82,99
 "entrees": [
    ("LAM2501", 5328.20, ""),
    ("LAM2502", 7000.00, ""),
 ],
 "depenses": [
    ("Collation - Plouf et Baballe",                      8.40, ""),
    ("Carburant",                                         22.90, "Q8 Easy Zaventem"),
    ("Réception marchandise - FEDEX",                     5.69, ""),
    ("Parking",                                           1.35, ""),
    ("Carburant",                                         62.79, "Cora Woluwe — à confirmer (carburant ou achats ?)"),
    ("Crédit voiture",                                    724.12, ""),
    ("Frais bancaires trimestriels",                      11.25, ""),
    ("Assurance voiture",                                 431.25, "Paiement par domiciliation (AG Insurance)"),
    ("Repas Topogigio",                                   22.00, ""),
    ("Carburant",                                         66.72, "Q8 Easy Zaventem"),
    ("Parking",                                           22.50, "Parking Centraal Anvers"),
    ("Parking",                                           1.80, "Commune Saint-Josse"),
    ("Electrabel",                                        256.99, ""),
    ("Telenet",                                           159.10, ""),
    ("Parking",                                           1.60, "Woluwe-Saint-Lambert"),
    ("Carburant",                                         71.13, "Cora Woluwe — à confirmer (carburant ou achats ?)"),
    ("Péage autoroute France",                            27.90, "Domiciliation Autoroutes du Sud de la France"),
    ("Parking",                                           7.20, "Parking Rogier"),
    ("Parking",                                           2.68, ""),
    ("Billets d'avion Pérou - Translatina Travel",        1100.00, "Facture de l'agence à joindre"),
    ("Précompte salarial janvier 2025 Thibault Duchène",  2250.00, ""),
    ("Billets d'avion Pérou - Translatina Travel",        42.00, "Complément — facture à joindre"),
    ("Carburant",                                         69.44, "Lukoil Wezembeek"),
    ("Impôt des sociétés",                                4517.28, "Communication 202/9987/63859"),
    ("Frais comptable BDH",                               1125.30, "Facture 20240512"),
    ("SD Worx",                                           331.52, ""),
    ("Frais comptable BDH",                               290.40, "Facture 20240616"),
    ("Frais comptable BDH",                               242.00, "Facture 20240705"),
    ("Proximus",                                          70.18, ""),
 ],
}))

MOIS.append(("Février", {
 "solde_debut": 3407.94, "solde_fin": 2468.17, "extrait": "2025 - 002",
 "entrees": [
    ("LAM2503", 5145.00, ""),
    ("Remboursement Electrabel", 256.99, "Remboursement du double paiement de la facture 468/9192/57548"),
 ],
 "depenses": [
    ("Achat vêtements sport - PVH Maasmechelen",          210.49, ""),
    ("Achat vêtements sport - NIKE Maasmechelen",         141.47, ""),
    ("Parking",                                           2.10, "Indigo Park Docks"),
    ("Electrabel",                                        256.99, "Facture 468/9192/57548 payée 2× (16-01 et 04-02) — remboursée le 10-02"),
    ("Telenet",                                           149.10, ""),
    ("Carburant",                                         65.00, "Dats 24 Nossegem"),
    ("Crédit voiture",                                    724.12, ""),
    ("Parking",                                           1.80, "Schaerbeek"),
    ("Parking",                                           6.20, "Administration communale Bruxelles"),
    ("Parking",                                           2.50, "Parking Ixelles - Gand"),
    ("Parking",                                           17.10, "Q-Park Heilig Hart Louvain"),
    ("Carburant",                                         69.47, "Q8 Easy Zaventem"),
    ("Transport - STIB",                                  4.60, ""),
    ("Transport - De Lijn",                               2.50, ""),
    ("Parking",                                           2.50, "Parkeren Louvain"),
    ("Parking",                                           1.80, "Commune Saint-Josse"),
    ("Partena",                                           1441.87, ""),
    ("Farys (eau)",                                       290.00, ""),
    ("Parking",                                           6.50, "Parking Ixelles - Gand"),
    ("Carburant",                                         68.61, "Q8 Easy Zaventem"),
    ("Repas Lunch Garden",                                39.47, "LG Auderghem"),
    ("Achat matériel sportif - DECATHLON",                140.00, "Decathlon Evere"),
    ("Précompte salarial février 2025 Thibault Duchène",  2250.00, ""),
    ("SD Worx",                                           331.52, ""),
    ("Carburant",                                         66.07, "Q8 Easy Zaventem"),
    ("Proximus",                                          49.98, ""),
 ],
}))

MOIS.append(("Mars", {
 "solde_debut": 2468.17, "solde_fin": 3606.60, "extrait": "2025 - 003",
 "entrees": [
    ("LAM2504", 5000.00, ""),
    ("LAM2505", 4888.80, ""),
 ],
 "depenses": [
    ("Achat - NEW BS SPRL",                               290.50, "Bruxelles — commerçant à identifier"),
    ("Crédit voiture",                                    724.12, ""),
    ("Repas Topogigio",                                   75.50, ""),
    ("Parking",                                           6.30, "Brucity - Ville de Bruxelles"),
    ("Carburant",                                         67.55, "Q8 Limal"),
    ("Paiement carte VISA",                               7.30, "Décompte n° 060"),
    ("Electrabel",                                        256.99, "Facture 470/3433/24753"),
    ("Electrabel",                                        256.99, "Facture 440/7222/59244"),
    ("Telenet",                                           149.40, ""),
    ("Redevance de stationnement - Ville de Louvain",     58.00, "Comm. 194/3769/90294 — à confirmer (redevance ou amende)"),
    ("Redevance de stationnement - Woluwe-Saint-Lambert", 45.00, "Comm. 602/2505/46621 — à confirmer (redevance ou amende)"),
    ("Parking",                                           1.85, "Q-Park Woluwe Esplanade"),
    ("Parking",                                           6.00, "T and T Parking Bruxelles"),
    ("Carburant",                                         60.74, "Q8 Easy Zaventem"),
    ("Parking",                                           2.67, "Commune Saint-Josse"),
    ("Carburant",                                         50.20, "Station 15 Zemst"),
    ("Partena",                                           3014.00, ""),
    ("Entretien voiture - Monsieur Pneus",                919.17, ""),
    ("Carburant",                                         70.68, "Shell Kraainem"),
    ("Carburant",                                         16.00, "Station 15 Zemst"),
    ("Parking",                                           16.20, "Parking Rogier"),
    ("Parking",                                           3.20, "Woluwe-Saint-Lambert"),
    ("Précompte salarial mars 2025 Thibault Duchène",     2250.00, ""),
    ("SD Worx",                                           331.52, ""),
    ("Carburant",                                         70.49, "Q8 Easy Zaventem"),
 ],
}))
