# Uloží žádné jméno a vypíše jej
jmeno = input("ZADEJ JMÉNO:")
print("Ukládám '", jmeno,"' do jmeno... ")

# Uloží případné příjmení a vypíše jej
prijmeni = input("ZADEJ PŘIJMENÍ: ")
print("Ukládám '", prijmeni, "' do prijmeni... ")


# Vytvoří proměnnou "cele_jmeno" obsahující mezeru a vypíše její obsah
cele_jmeno = jmeno + " " + prijmeni
print("Celé jméno:", cele_jmeno)

# Vytvoří a vypíše hodnotu délky uložené proměnné "cele_jmeno"
delka_jmena = (len(cele_jmeno)) - 1
print(delka_jmena)

# Vypíše celé jméno ohraničené oddělovači
print("=" * delka_jmena)
print(cele_jmeno)
print("=" * delka_jmena)
