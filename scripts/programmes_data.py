# -*- coding: utf-8 -*-
"""Donnees des programmes, transcrites des feuilles manuscrites.

Conventions :
- terrain prive facture 525 EUR/heure en prix normal, "Gratuit" en prix adapte ;
- physique, semi-prive et collectifs laisses a completer ;
- League Cup a 250 EUR en prix normal ;
- rassemblements, stages et entrainements dans un autre club : en remarque,
  jamais de ligne dans le tableau.
"""

PROGRAMMES = {
    "Petra_NAGY": {
        "titre": "Programme Petra NAGY",
        "planning": [
            "Lundi : Privé 16h – 17h (Yassine)",
            "Mercredi : Collectif 14h – 15h (Yassine)",
            "Vendredi : Privé 16h – 17h (Yassine)",
            "Samedi : Physique sur terrain 10h – 11h (avec Guillaume) et Collectif 11h – 12h (avec Adel)",
        ],
        "note": "Les cours privés (lundi et vendredi) sont à payer directement à Yassine.",
        "tableau": [
            ("2h de terrains (privés)", "1050", "Gratuit"),
            ("1h de physique", "………", "Gratuit"),
            ("Collectif 2h", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Djena": {
        "titre": "Programme Djena",
        "planning": [
            "Mercredi : Physique 14h – 15h30 (avec Loïc) et Privé 17h30 – 18h30 (Yassine)",
            "Jeudi : Collectif 17h30 – 19h (avec Taha)",
            "Samedi : Physique sur terrain 11h – 12h (avec Guillaume) et League Cup 15h – 16h30",
        ],
        "note": "Le cours privé (mercredi) est à payer directement à Yassine.",
        "tableau": [
            ("1h de terrain (privé)", "525", "Gratuit"),
            ("1h30 de physique", "………", "………"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 1h30", "………", "………"),
            ("League Cup", "250", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Noah_Vicente": {
        "titre": "Programme Noah Vicente",
        "planning": [
            "Lundi : Privé 16h – 17h (Thibault)",
            "Mercredi : Semi-privé 13h30 – 14h30 avec Samuel (Thibault)",
            "Jeudi : Collectif 16h30 – 17h30 (avec Taha)",
            "Samedi : Rassemblement 13h30 – 15h",
        ],
        "note": "Le cours privé (lundi) et le semi-privé (mercredi) sont à payer directement à Thibault.",
        "remarques": [
            "Le rassemblement du samedi (13h30 – 15h) n'est pas repris dans le tableau.",
        ],
        "tableau": [
            ("1h de terrain (privé)", "525", "Gratuit"),
            ("1h de semi-privé", "………", "………"),
            ("Collectif 1h", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Aleksander_LUKACHI": {
        "titre": "Programme Aleksander LUKACHI",
        "planning": [
            "Lundi : Physique 16h45 – 18h15 (avec Loïc)",
            "Mardi : Privé 16h30 – 17h30 (Yassine)",
            "Mercredi : Collectif 16h – 17h30 (avec Julien)",
            "Jeudi : Collectif 17h – 18h30 (avec Yassine)",
            "Samedi : Physique sur terrain 10h – 11h (avec Guillaume) et League Cup 15h – 16h30",
        ],
        "note": "Le cours privé (mardi) est à payer directement à Yassine.",
        "tableau": [
            ("1h de terrain (privé)", "525", "Gratuit"),
            ("1h30 de physique", "………", "………"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 3h", "………", "………"),
            ("League Cup", "250", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Thomas_WAGNER": {
        "titre": "Programme Thomas WAGNER",
        "planning": [
            "Lundi : Collectif 17h – 18h30 (avec Thibault)",
            "Mercredi : Privé 17h30 – 19h (Thibault, sparring Lucas Smets)",
            "Jeudi : Semi-privé 16h30 – 18h30 avec Gus (Thibault)",
            "Vendredi : Privé 16h30 – 17h30 (Thibault)",
            "Samedi : Orée",
        ],
        "note": "Les cours privés (mercredi et vendredi) et le semi-privé (jeudi) sont à payer directement à Thibault.",
        "remarques": [
            "Le rassemblement à Wallis et le samedi à l'Orée se déroulent dans d'autres clubs : ils ne sont pas repris dans le tableau.",
            "Physique ADEPS à confirmer (2 séances ?).",
        ],
        "tableau": [
            ("2h30 de terrains (privés)", "1312", "Gratuit"),
            ("2h de semi-privé", "………", "………"),
            ("Collectif 1h30", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Maxim_BEKCHIEV": {
        "titre": "Programme Maxim BEKCHIEV",
        "planning": [
            "Lundi : Collectif 17h30 – 19h (avec Taha)",
            "Mardi : Collectif 17h30 – 19h (avec Pascal)",
            "Mercredi : Physique 15h – 16h30 (avec Loïc)",
            "Jeudi : repos",
            "Vendredi : Privé ou collectif (gratuit)",
            "Samedi : Physique sur terrain 11h – 12h (avec Guillaume), Privé 12h – 13h (Yassine) et League Cup 15h – 16h30",
            "Dimanche : possibilité de privé 17h – 18h30",
        ],
        "note": "Le cours privé (samedi) est à payer directement à Yassine.",
        "remarques": [
            "Le privé du dimanche est une possibilité : il n'est pas repris dans le tableau.",
            "Le vendredi (privé ou collectif) est gratuit.",
        ],
        "tableau": [
            ("1h de terrain (privé)", "525", "Gratuit"),
            ("1h30 de physique", "………", "………"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 3h", "………", "………"),
            ("League Cup", "250", "………"),
            ("Total", "………", "………"),
        ],
    },
    "David_VAN_BOMMEL": {
        "titre": "Programme David VAN BOMMEL",
        "planning": [
            "Mercredi : Physique 15h30 – 17h (avec Loïc)",
            "Jeudi : Collectif 17h – 18h30 (avec Yassine)",
            "Samedi : Physique sur terrain 11h – 12h (avec Guillaume) et League Cup 15h – 16h30",
        ],
        "note": None,
        "tableau": [
            ("1h30 de physique", "………", "………"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 1h30", "………", "………"),
            ("League Cup", "250", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Samuel_VAN_BOMMEL": {
        "titre": "Programme Samuel VAN BOMMEL",
        "planning": [
            "Mercredi : Semi-privé 13h30 – 14h30 avec Noah (Thibault) et Physique 15h30 – 17h (avec Loïc)",
            "Jeudi : Collectif 16h30 – 17h30 (avec Taha)",
            "Samedi : Rassemblement 13h30 – 15h",
        ],
        "note": "Le semi-privé (mercredi) est à payer directement à Thibault.",
        "remarques": [
            "Le rassemblement du samedi (13h30 – 15h) n'est pas repris dans le tableau.",
        ],
        "tableau": [
            ("1h de semi-privé", "………", "………"),
            ("1h30 de physique", "………", "………"),
            ("Collectif 1h", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Valeria_POVEZDHA": {
        "titre": "Programme Valeria POVEZDHA",
        "planning": [
            "Lundi : Physique 16h45 – 18h15 (avec Loïc)",
            "Mercredi : Privé 12h30 – 13h30 (Julien) et Physique 15h30 – 17h (avec Loïc)",
            "Vendredi : Semi-privé 17h30 – 19h (avec Julien)",
        ],
        "note": "Le cours privé (mercredi) et le semi-privé (vendredi) sont à payer directement à Julien.",
        "tableau": [
            ("1h de terrain (privé)", "525", "Gratuit"),
            ("1h30 de semi-privé", "………", "………"),
            ("3h de physique", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Maxim_GROZDEV": {
        "titre": "Programme Maxim GROZDEV",
        "planning": [
            "Mercredi : Privé 13h30 – 14h30 (Julien)",
            "Vendredi : Privé 15h30 – 16h30 (Thibault)",
        ],
        "note": "Le cours privé du mercredi est à payer directement à Julien, celui du vendredi à Thibault.",
        "tableau": [
            ("2h de terrains (privés)", "1050", "Gratuit"),
            ("Total", "1050", "………"),
        ],
    },
    "Huseyin_BOZKIR": {
        "titre": "Programme Huseyin BOZKIR",
        "planning": [
            "Lundi : Collectif 17h – 18h30 (avec Thibault)",
            "Mercredi : Privé 14h30 – 16h (Thibault)",
            "Samedi : Orée",
        ],
        "note": "Le cours privé (mercredi) est à payer directement à Thibault.",
        "remarques": [
            "Le rassemblement à Wallis et le samedi à l'Orée se déroulent dans d'autres clubs : ils ne sont pas repris dans le tableau.",
            "Physique à définir.",
        ],
        "tableau": [
            ("1h30 de terrain (privé)", "787", "Gratuit"),
            ("Collectif 1h30", "………", "Gratuit"),
            ("Total", "………", "………"),
        ],
    },
    "Gus_DENIS": {
        "titre": "Programme Gus DENIS",
        "planning": [
            "Lundi : Privé 10h30 – 11h30 (Thibault) et Collectif 17h – 18h30 (avec Thibault)",
            "Mercredi : Physique 14h – 15h30 (avec Loïc) et Privé 16h – 17h30 (Thibault)",
            "Jeudi : Semi-privé 16h30 – 18h30 avec Thomas (Thibault)",
            "Vendredi : Rassemblement 19h – 20h30",
            "Samedi : Orée",
        ],
        "note": "Les cours privés (lundi et mercredi) et le semi-privé (jeudi) sont à payer directement à Thibault.",
        "remarques": [
            "Le rassemblement du vendredi (19h – 20h30) et le samedi à l'Orée ne sont pas repris dans le tableau.",
            "Physique ADEPS à confirmer.",
        ],
        "tableau": [
            ("2h30 de terrains (privés)", "1312", "Gratuit"),
            ("2h de semi-privé", "………", "………"),
            ("1h30 de physique", "………", "………"),
            ("Collectif 1h30", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Ediz_BOZKIR": {
        "titre": "Programme Ediz BOZKIR",
        "planning": [
            "Mardi : Privé 16h – 17h (Julien)",
            "Mercredi : Physique 14h – 15h30 (avec Loïc) et Collectif 16h – 17h30 (avec Julien)",
            "Jeudi : Collectif 17h30 – 19h (avec Julien)",
            "Vendredi : Semi-privé 16h – 17h30 avec Gaspard (Julien)",
            "Samedi : Physique sur terrain 10h – 11h (avec Guillaume) et League Cup 15h – 16h30",
        ],
        "note": "Le cours privé (mardi) et le semi-privé (vendredi) sont à payer directement à Julien.",
        "tableau": [
            ("1h de terrain (privé)", "525", "Gratuit"),
            ("1h30 de semi-privé", "………", "………"),
            ("1h30 de physique", "………", "………"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 3h", "………", "………"),
            ("League Cup", "250", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Vytautas_RAZAUSKAS": {
        "titre": "Programme Vytautas RAZAUSKAS",
        "planning": [
            "Lundi : Collectif 18h30 – 20h (avec Yassine)",
            "Mardi : Privé 16h – 17h30 (Thibault)",
            "Mercredi : Physique 14h – 15h30 (avec Loïc)",
            "Vendredi : Rassemblement 19h – 20h30 (Thibault)",
            "Samedi : Physique sur terrain 11h – 12h (avec Guillaume) et League Cup 15h – 16h30",
        ],
        "note": "Le cours privé (mardi) est à payer directement à Thibault.",
        "remarques": [
            "Le rassemblement du vendredi (19h – 20h30) n'est pas repris dans le tableau.",
        ],
        "tableau": [
            ("1h30 de terrain (privé)", "787", "Gratuit"),
            ("1h30 de physique", "………", "………"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 1h30", "………", "………"),
            ("League Cup", "250", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Martin_GENTCHEV": {
        "titre": "Programme Martin GENTCHEV",
        "planning": [
            "Lundi : Physique 16h45 – 18h15 (avec Loïc) et Collectif 18h30 – 20h (avec Yassine)",
            "Mardi : Privé 17h30 – 19h (Thibault)",
            "Mercredi : Physique 14h – 15h30 (avec Loïc)",
            "Vendredi : Rassemblement 19h – 20h30 (Thibault)",
            "Samedi : Physique sur terrain 11h – 12h (avec Guillaume) et League Cup 15h – 16h30",
        ],
        "note": "Le cours privé (mardi) est à payer directement à Thibault.",
        "remarques": [
            "Le rassemblement du vendredi (19h – 20h30) n'est pas repris dans le tableau.",
        ],
        "tableau": [
            ("1h30 de terrain (privé)", "787", "Gratuit"),
            ("3h de physique", "………", "………"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 1h30", "………", "………"),
            ("League Cup", "250", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Alexandra_GENTCHEVA": {
        "titre": "Programme Alexandra GENTCHEVA",
        "planning": [
            "Lundi : Physique 16h45 – 18h15 (avec Loïc)",
            "Vendredi : Semi-privé 17h30 – 19h (avec Julien)",
            "Samedi : Physique sur terrain 10h – 11h (avec Guillaume) et Collectif 11h – 12h30 (avec Celia)",
        ],
        "note": "Le semi-privé (vendredi) est à payer directement à Julien.",
        "tableau": [
            ("1h30 de semi-privé", "………", "………"),
            ("1h30 de physique", "………", "………"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 1h30", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Vladimir_LUKACHI": {
        "titre": "Programme Vladimir LUKACHI",
        "planning": [
            "Mardi : Collectif 17h – 18h30 (avec Julien)",
            "Mercredi : Collectif 14h30 – 16h (avec Julien)",
            "Jeudi : Privé 16h – 17h (Yassine)",
            "Samedi : Physique sur terrain 10h – 11h (avec Guillaume) et Rassemblement 13h30 – 15h",
        ],
        "note": "Le cours privé (jeudi) est à payer directement à Yassine.",
        "remarques": [
            "Le rassemblement du samedi (13h30 – 15h) n'est pas repris dans le tableau.",
        ],
        "tableau": [
            ("1h de terrain (privé)", "525", "Gratuit"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 3h", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Leo_MORENO_GALAN": {
        "titre": "Programme Leo Moreno Galan",
        "planning": [
            "Lundi : Collectif 18h30 – 20h (avec Yassine)",
            "Mercredi : Physique 14h – 15h30 (avec Loïc)",
            "Vendredi : Rassemblement 19h – 20h30 (Thibault)",
            "Samedi : Physique sur terrain 11h – 12h (avec Guillaume) et Collectif 13h30 – 15h",
        ],
        "note": None,
        "remarques": [
            "Le coach du collectif du samedi (13h30 – 15h) reste à confirmer.",
            "Le rassemblement du vendredi (19h – 20h30) n'est pas repris dans le tableau.",
        ],
        "tableau": [
            ("1h30 de physique", "………", "………"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 3h", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Adrien": {
        "titre": "Programme Adrien",
        "planning": [
            "Vendredi : Privé 14h – 15h30 (Taha) et Rassemblement 19h – 20h30",
            "Samedi : Jeu de jambes 11h – 12h et Collectif 13h30 – 15h",
        ],
        "note": "Le cours privé (vendredi) est à payer directement à Taha.",
        "remarques": [
            "Le rassemblement du vendredi (19h – 20h30) n'est pas repris dans le tableau.",
        ],
        "tableau": [
            ("1h30 de terrain (privé)", "787", "Gratuit"),
            ("1h de jeu de jambes", "………", "………"),
            ("Collectif 1h30", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Gaspard_STAS": {
        "titre": "Programme Gaspard STAS",
        "planning": [
            "Lundi : Collectif 17h30 – 19h (avec Taha)",
            "Mercredi : Collectif 16h – 17h30 (avec Julien)",
            "Vendredi : Semi-privé 16h – 17h30 avec Ediz (Julien)",
            "Samedi : Physique sur terrain 11h – 12h (avec Guillaume)",
        ],
        "note": "Le semi-privé (vendredi) est à payer directement à Julien.",
        "tableau": [
            ("1h30 de semi-privé", "………", "………"),
            ("1h de physique sur terrain", "………", "Gratuit"),
            ("Collectif 3h", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
    "Lucas_WOZNY": {
        "titre": "Programme Lucas WOZNY",
        "planning": [
            "Lundi : Physique 16h45 – 18h15 (avec Loïc)",
            "Mardi : Collectif 17h – 18h30 (avec Julien)",
            "Mercredi : Collectif 14h30 – 16h (avec Julien)",
            "Vendredi : Privé 15h – 16h (Yassine)",
            "Samedi : Rassemblement 13h30 – 15h",
        ],
        "note": "Le cours privé (vendredi) est à payer directement à Yassine.",
        "remarques": [
            "Le rassemblement du samedi (13h30 – 15h) n'est pas repris dans le tableau.",
        ],
        "tableau": [
            ("1h de terrain (privé)", "525", "Gratuit"),
            ("1h30 de physique", "………", "………"),
            ("Collectif 3h", "………", "………"),
            ("Total", "………", "………"),
        ],
    },
}
