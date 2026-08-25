#!/usr/bin/env python3
"""Convertit un montant entier en euros en toutes lettres, en français de Belgique.

Belgique : septante (70), quatre-vingts (80), nonante (90).
Usage : python euros_en_lettres.py 28176
        -> vingt-huit mille cent septante-six
"""
import sys

UNITES = [
    "zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit",
    "neuf", "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize",
    "dix-sept", "dix-huit", "dix-neuf",
]
DIZAINES = {
    20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante",
    60: "soixante", 70: "septante", 80: "quatre-vingt", 90: "nonante",
}


def _sous_cent(n: int) -> str:
    if n < 20:
        return UNITES[n]
    d, u = (n // 10) * 10, n % 10
    if d == 80:
        # quatre-vingts si rien derrière, quatre-vingt-un (pas de "et")
        return "quatre-vingts" if u == 0 else f"quatre-vingt-{UNITES[u]}"
    base = DIZAINES[d]
    if u == 0:
        return base
    if u == 1:  # vingt et un, ... septante et un, nonante et un
        return f"{base} et un"
    return f"{base}-{UNITES[u]}"


def _sous_mille(n: int) -> str:
    if n == 0:
        return ""
    c, reste = n // 100, n % 100
    if c == 0:
        return _sous_cent(reste)
    # "cent" au singulier si multiplicateur 1 ; "cents" pluriel seulement si rien derrière
    if c == 1:
        tete = "cent"
    else:
        tete = f"{UNITES[c]} cents" if reste == 0 else f"{UNITES[c]} cent"
    return tete if reste == 0 else f"{tete} {_sous_cent(reste)}"


def en_lettres(n: int) -> str:
    if n == 0:
        return "zéro"
    parts = []
    millions, reste = divmod(n, 1_000_000)
    milliers, centaines = divmod(reste, 1000)
    if millions:
        parts.append("un million" if millions == 1 else f"{_sous_mille(millions)} millions")
    if milliers:
        parts.append("mille" if milliers == 1 else f"{_sous_mille(milliers)} mille")
    if centaines:
        parts.append(_sous_mille(centaines))
    return " ".join(parts)


def euros_en_lettres(n: int) -> str:
    return f"{en_lettres(n)} euros"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python euros_en_lettres.py <montant_entier>", file=sys.stderr)
        sys.exit(1)
    print(euros_en_lettres(int(sys.argv[1])))
