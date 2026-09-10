# -*- coding: utf-8 -*-
# Données 2025 — reprises des extraits de compte BNP Paribas Fortis
# BE23 0019 5419 0591 — BV MT COSMETICS BELGIUM
#
# Convention retenue : les opérations débitées/créditées début janvier 2025 mais
# se rapportant à décembre 2024 (et déjà encodées dans le bilan 2024) sont
# EXCLUES de 2025. Le total du mois ne correspond donc volontairement pas à la
# variation de solde de l'extrait bancaire.

MOIS = [("Janvier", {
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
})]
