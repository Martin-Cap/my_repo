# Vstupní hodnoty
MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = "=" * 35

# Uvítání uživatele
print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(ODDELOVAC)

# Vložení údaje
print(
"""
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
)
print(ODDELOVAC)
lokalita = int(input("VYBERTE CISLO LOKALITY:"))

# Úprava zadané hodnoty
destinace = MESTA[lokalita - 1]
cena = CENY[lokalita - 1]

# Vypsání výstupu
print("LISTEK DO:", destinace, "CENA:", cena)
#print("DEKUJI,", jmeno, "NA MAIL", email, "TI PRIJDE KRATKY DOTAZNIK")
