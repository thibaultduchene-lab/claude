---
name: facture-stages-commune
description: >-
  Génère la facture Word que le RTC Lambermont envoie à la Commune de Schaerbeek
  (ASBL OCS, Œuvre des Colonies Scolaires) pour les enfants « COMMUNE » inscrits
  aux stages de tennis. À utiliser dès que Thibault demande de préparer, générer,
  refaire ou mettre à jour une « facture commune », « facture OCS », « facture
  stages », de facturer les stages à la commune/Schaerbeek/OCS, ou de produire le
  document OCS0xx — même sans dire explicitement « skill » ou « facture ». Couvre
  aussi le calcul du total, des sous-totaux par semaine et du montant en toutes
  lettres (français de Belgique).
---

# Facture stages → Commune de Schaerbeek (OCS)

Chaque période de stages (été, Toussaint, Carnaval, Pâques…), l'école de tennis du
Lambermont facture à la Commune de Schaerbeek les enfants inscrits **via la
commune**. Ce skill produit le `.docx` prêt à envoyer, à l'identique de la mise en
forme habituelle, et fiabilise les deux points qui coûtent le plus d'erreurs : le
total et le montant en toutes lettres.

La facture de référence (`assets/Facture_OCS026_reference.docx`, été 2026) sert de
modèle visuel — ouvre-la en cas de doute sur le rendu attendu.

## La règle qui prime : uniquement les enfants « COMMUNE »

Seules les inscriptions payées par la commune figurent sur cette facture. Dans les
listes d'inscrits, ce sont les enfants dont le nom porte le suffixe **`(COMMUNE)`**.
Les enfants inscrits en direct (payés par les parents au club) ne doivent **jamais**
apparaître ici. Si tu pars d'une liste complète d'inscrits, commence par filtrer sur
`(COMMUNE)` ; en cas de doute sur une ligne, demande plutôt que d'inclure à tort —
une facture gonflée envoyée à la commune est pénible à corriger.

## Ce dont tu as besoin avant de générer

Demande (ou récupère dans la conversation) :

1. **Le numéro de facture** — format `OCS0xx`, incrémenté à partir de la dernière
   facture émise. La dernière connue est **OCS026** (été 2026) ; la suivante serait
   `OCS027`. Confirme toujours le numéro, ne le devine pas seul.
2. **La période et son libellé** — sert à la ligne « Concerne » et au regroupement
   par semaine. Ex. été = « Eté 2 à 8 (06/07/2026-21/08/2026) ».
3. **La liste des inscriptions à facturer**, par semaine : nom, prénom, formule.
4. **Les semaines à tarif réduit** (voir Tarifs) — à confirmer explicitement.

## Tarifs

- **120 € par enfant et par semaine** en temps normal (une semaine = 5 jours).
- **Tarif réduit quand un jour férié écourte la semaine.** Sur OCS026, la Semaine 4
  était à **96 €** car le 21/07 (fête nationale belge) tombait dedans : 4 jours au
  lieu de 5, soit 120 × 4/5 = 96. Applique la même logique (`120 × jours_ouvrés / 5`,
  arrondi à l'entendu habituel) et **fais confirmer** quelles semaines sont réduites
  avant de générer — c'est spécifique à chaque calendrier.

Le montant est porté par ligne dans le CSV (colonne `montant`), ce qui permet de
mélanger semaines pleines et réduites sans réglage global.

## Formules (libellés exacts, ordre d'affichage dans chaque semaine)

Reprends ces intitulés **au caractère près** — ils apparaissent tels quels sur la
facture et servent aussi à ordonner les lignes :

1. `Stage Découverte du Tennis 3 - 5ans`
2. `Stage Mini-Tennis - 5 - 7ans`
3. `Stage Tennis - Multisports - 8 à 18 ans`
4. `Stage Compétition - 7 à 18 ans`

Une formule inédite est possible (nouvelle offre) : garde le style « Stage … - âge »
et signale-la, elle sera placée en fin de semaine.

## Coordonnées fixes (déjà codées dans le script, ne pas retaper)

- **Destinataire :** Commune de Schaerbeek ASBL OCS, Œuvre des Colonies Scolaire
  78-80, 1030 Schaerbeek
- **Compte / IBAN :** BE48068942393827
- **Signataire :** Thibault Duchène — Directeur de l'école de tennis du Lambermont
- **En-tête :** logo `assets/entete_lambermont.png` (RTC Lambermont)

Si l'une de ces valeurs a changé, mets-la à jour dans `scripts/build_facture.py` (en
tête de fichier) plutôt qu'à la main dans le document.

## Comment générer

1. **Construis le CSV** des inscriptions à facturer, une ligne par enfant/semaine :

   ```csv
   semaine,nom,prenom,formule,montant
   Semaine 2,CHAABANE (COMMUNE),Jad,Stage Découverte du Tennis 3 - 5ans,120
   Semaine 4,BARRY (COMMUNE),Hamid,Stage Découverte du Tennis 3 - 5ans,96
   ```

   Le libellé de `semaine` est libre (« Semaine 2 », « Toussaint », …) ; les semaines
   s'affichent dans leur ordre d'apparition, et à l'intérieur d'une semaine le script
   trie par formule puis par nom.

2. **Lance le générateur** :

   ```bash
   cd .claude/skills/facture-stages-commune/scripts
   python build_facture.py <chemin_csv> \
     --numero OCS027 \
     --concerne "stages découverte du tennis 3-5 ans, mini-tennis 5-7 ans et tennis/multisports, Toussaint 2026 (25/10/2026-31/10/2026)" \
     --sortie Facture_OCS027.docx
   ```

   Le script calcule les sous-totaux par semaine, le total, et le montant en toutes
   lettres (belge), puis écrit le `.docx`. Dépendance : `python-docx`
   (`pip install python-docx` si absent).

3. **Vérifie avant d'envoyer.** Le script affiche le nombre d'inscriptions, le total
   et le montant en lettres. Recoupe le total avec ton propre calcul
   (`nb × tarif` par semaine) — une facture pour la commune doit être juste du
   premier coup. Ouvre le `.docx` pour un contrôle visuel rapide.

## Montant en toutes lettres

`scripts/euros_en_lettres.py` convertit un entier en euros en **français de
Belgique** : *septante* (70), *quatre-vingts* (80), *nonante* (90). Ex.
`28176 → vingt-huit mille cent septante-six euros`. Le générateur l'utilise déjà ;
tu peux aussi l'appeler seul : `python euros_en_lettres.py 12345`.

## Fichiers du skill

- `scripts/build_facture.py` — génère le `.docx` depuis le CSV.
- `scripts/euros_en_lettres.py` — nombre → toutes lettres (belge).
- `assets/Facture_OCS026_reference.docx` — facture de référence (été 2026).
- `assets/entete_lambermont.png` — logo d'en-tête.
