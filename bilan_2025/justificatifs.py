# -*- coding: utf-8 -*-
"""Tickets et factures reçus, rattachés à leur ligne du bilan.

Une entrée = (mois, libellé exact de la dépense, montant, nom du PDF).
La colonne « Facture » passe à V et le nom du justificatif est ajouté en
remarque. Les PDF sont dans ../justificatifs_2025/.

PHOTOS = (fichier source, nom du PDF) — sert à (re)générer les PDF.
"""

PHOTOS = [
 ("8974c09d", "2025-01-10_RTCL-Lambermont_22.00.pdf"),
 ("ee7298c6", "2025-02-01_Nike-Maasmechelen_141.47.pdf"),
 ("0001bc95", "2025-02-01_TommyHilfiger-Maasmechelen_210.49.pdf"),
 ("2f337163", "2025-02-22_LunchGarden-Kraainem_39.47.pdf"),
 ("1f5fd196", "2025-02-25_Decathlon-Evere_140.00.pdf"),
 ("9e8e77c5", "2025-03-05_RTCL-Lambermont_75.50.pdf"),
 ("58d12057", "2025-03-20_Station15-Zemst_50.20.pdf"),
 ("3a2a53b0", "2025-03-25_MonsieurPneus_919.17.pdf"),
 ("e2ab44a6", "2025-03-27_Station15-Zemst_16.00.pdf"),
 ("c62e3f14", "2025-04-01_EXKi-Woluwe_30.30.pdf"),
 ("ae70bf93", "2025-04-06_NZA-Utrecht_289.97.pdf"),
 ("5b35d27c", "2025-04-23_RTCL-Lambermont_29.00_SANS-CORRESPONDANCE.pdf"),
 ("1126abc6", "2025-04-26_Decathlon-Evere_84.20.pdf"),
 ("8bc4b27f", "2025-05-12_Decathlon-Evere_50.00.pdf"),
 ("f18136dd", "2025-06-02_Decathlon-Evere_200.00.pdf"),
 ("5bd6587e", "2025-07-10_Oree-ASBL_8.50.pdf"),
 ("97e929e3", "2025-07-25_RTCL-Lambermont_251.50_SANS-CORRESPONDANCE.pdf"),
 ("70a117ca", "2025-08-08_Decathlon-Evere_18.00.pdf"),
 ("c7461563", "2025-08-14_Decathlon-Evere_123.00.pdf"),
 ("f2cf9d87", "2025-09-13_LunchGarden-Kraainem_45.77.pdf"),
 ("1a1d1b79", "2025-09-19_EXKi-Woluwe_35.40.pdf"),
 ("de17fb45", "2025-09-23_ChezJi-Peruwelz_47.00.pdf"),
 ("5beae4f2", "2025-09-25_FedEx_17.37.pdf"),
 ("8a996caf", "2025-09-26_TotalEnergies-Nivelles_13.65.pdf"),
 ("0b5cea9d", "2025-09-27_Bellissimo-Sport_40.00.pdf"),
 ("21f44f1f", "2025-10-29_RTCL-Lambermont_58.00.pdf"),
 ("bbeee85e", "2025-11-22_Decathlon-Evere_118.50.pdf"),
 ("e6aeb750", "2025-12-23_FedEx_11.84_SANS-CORRESPONDANCE.pdf"),
]

JUSTIFICATIFS = [
 ("Janvier",   "Repas Topogigio",                                    22.00,  "2025-01-10_RTCL-Lambermont_22.00.pdf"),
 ("Février",   "Achat vêtements sport - NIKE Maasmechelen",          141.47, "2025-02-01_Nike-Maasmechelen_141.47.pdf"),
 ("Février",   "Achat vêtements sport - Tommy Hilfiger Maasmechelen",210.49, "2025-02-01_TommyHilfiger-Maasmechelen_210.49.pdf"),
 ("Février",   "Repas Lunch Garden",                                 39.47,  "2025-02-22_LunchGarden-Kraainem_39.47.pdf"),
 ("Février",   "Achat vêtement sport - DECATHLON",                   140.00, "2025-02-25_Decathlon-Evere_140.00.pdf"),
 ("Mars",      "Repas Topogigio",                                    75.50,  "2025-03-05_RTCL-Lambermont_75.50.pdf"),
 ("Mars",      "Carburant",                                          50.20,  "2025-03-20_Station15-Zemst_50.20.pdf"),
 ("Mars",      "Entretien voiture - Monsieur Pneus",                 919.17, "2025-03-25_MonsieurPneus_919.17.pdf"),
 ("Mars",      "Carburant",                                          16.00,  "2025-03-27_Station15-Zemst_16.00.pdf"),
 ("Avril",     "Repas Exki",                                         30.30,  "2025-04-01_EXKi-Woluwe_30.30.pdf"),
 ("Avril",     "Achat vêtements - N.Z.A. Utrecht",                   289.97, "2025-04-06_NZA-Utrecht_289.97.pdf"),
 ("Avril",     "Achat matériel sportif - DECATHLON",                 84.20,  "2025-04-26_Decathlon-Evere_84.20.pdf"),
 ("Mai",       "Achat matériel sportif - DECATHLON",                 50.00,  "2025-05-12_Decathlon-Evere_50.00.pdf"),
 ("Juin",      "Achat matériel sportif - DECATHLON",                 200.00, "2025-06-02_Decathlon-Evere_200.00.pdf"),
 ("Juillet",   "Consommation club de tennis Orée",                   8.50,   "2025-07-10_Oree-ASBL_8.50.pdf"),
 ("Août",      "Achat matériel sportif - DECATHLON",                 18.00,  "2025-08-08_Decathlon-Evere_18.00.pdf"),
 ("Août",      "Achat matériel sportif - DECATHLON",                 123.00, "2025-08-14_Decathlon-Evere_123.00.pdf"),
 ("Septembre", "Repas Lunch Garden",                                 45.77,  "2025-09-13_LunchGarden-Kraainem_45.77.pdf"),
 ("Septembre", "Repas Exki",                                         35.40,  "2025-09-19_EXKi-Woluwe_35.40.pdf"),
 ("Septembre", "Repas - Chez Ji SPRL",                               47.00,  "2025-09-23_ChezJi-Peruwelz_47.00.pdf"),
 ("Septembre", "Repas - TotalEnergies Nivelles",                     13.65,  "2025-09-26_TotalEnergies-Nivelles_13.65.pdf"),
 ("Septembre", "Achat matériel sportif - Bellissimo Sport",          40.00,  "2025-09-27_Bellissimo-Sport_40.00.pdf"),
 ("Octobre",   "Réception marchandise - FEDEX",                      17.37,  "2025-09-25_FedEx_17.37.pdf"),
 ("Octobre",   "Consommation Lambermont",                            58.00,  "2025-10-29_RTCL-Lambermont_58.00.pdf"),
 ("Novembre",  "Achat matériel sportif - DECATHLON",                 118.50, "2025-11-22_Decathlon-Evere_118.50.pdf"),
]

# Tickets reçus sans ligne correspondante dans le bilan — à trancher :
#   2025-04-23 RTCL Lambermont 29,00  : l'extrait ne montre que 26,00 ce jour-là
#   2025-07-25 RTCL Lambermont 251,50 : l'extrait ne montre que 231,50 (SumUp)
#   2025-12-23 FedEx 11,84            : facture de fin décembre, payée en 2026
