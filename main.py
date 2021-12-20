# vlozeni textu ze zadani projektu
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# 1. vytvarim slovnik existujicich uzivatelskych udaju:
users = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}
line = "-" # oddelovac
# 2. vyzaduji vstupy od uzivatele:
username = input("Choose username: ")
# podminky pro zadani uzivatelskych udaju
if username in users.keys(): # klice ze slovniku users
    password = input("Choose password: ")
    if password in users.values(): # porovnavam password od uzivatele s hodnotami ze slovniku users
        print(f"password: {password}\n"f"username: {username}\n{line*40}")
        print(f"Welcome to the app, {username}\nWe have 3 texts to be analyzed.\n{line*40}")
        user_choice = input("Enter a number btw. 1 and 3 to select: ")

# PRVNI VOLBA UZIVATELE

# rozdeleni slov podle mezer a ulozeni do seznamu "words_list"
        if user_choice == "1":  # podminka pokud si uzivatel vzbere prvni volbu
            words_list = TEXTS[0].split()   # vybiram ze seznamu TEXTS s indexem 0, tedy prvni text
            cista_slova = [] # zakladam novy seznam
            for slovo in words_list: # podminka pro nove ziskavana slova, ktera vytvarim ze seznamu vygenerovaneho z TEXTS[0]
                ciste = slovo.strip(".,")   # vytvarim 'cista' slova tak, ze z listu words_list odeberu '.' a ','
                cista_slova.append(ciste) # pripojim vznikla 'cista' slova, tedy vse bez '.' a ',', k prazdnemu seznamu cista_slova
            words_count = len(cista_slova) # ziskam celkovy pocet prvku v seznamu cista_slova

            print(f"There are {str(words_count)} words in the selected text.") # tisk poctu slov

# pocet slov napsanych velkym pismenem
            title_count = 0 # vytvarim promennou title_count, ktera bude zacinat od 0 a bude se k nim pricitava, pokud jsou splneny podminky nize
            for elem_title in words_list: # vytvarim promenne elem_title z listu words_count
                if elem_title.istitle(): # pokud je splnena podminka, ze slova z words_listu, resp. elem_title jsou na zacatku s vekym pismenem, prictu vzdy 1 k promenne title_count
                    title_count += 1
                continue # titmto preskocim, jiz nalezene
            print(f"There are {title_count} titlecase words.") # vypis

# pocet slov na zacatku s velkym pismenem
            upper_count = 0 # celkovy pocet zacina na nule a nasledne se navysuje
            for elem_upper in words_list: # nova promena vytvarena ze seznamu
                if elem_upper.isupper(): # podminka pro vyber vsech slov s velkym pismenem na zacatku
                    upper_count += 1 # pricitam nalezena slova
                continue

            print(f"There are {upper_count} uppercase words.")

# pocet slov na zacatku s malym pismenem
            lower_count = 0 # celkovy pocet zacina na nule a nasledne se navysuje
            for elem_lower in words_list: # nova promena vytvarena ze seznamu
                if elem_lower.islower(): # podminka pro vyber vsech slov s malym pismenem na zacatku
                    lower_count += 1 # pricitam nalezena slova
                continue
            print(f"There are {lower_count} lowercase words.")

# pocet 'cislenych' slov
            numeric_count = 0 # celkovy pocet zacina na nule a nasledne se navysuje
            for elem_numeric in words_list: # nova promena vytvarena ze seznamu
                if elem_numeric.isnumeric(): # podminka pro vyber vsech slov s malym pismenem na zacatku
                    numeric_count += 1  # pricitam nalezena slova
                continue
            print(f"There are {numeric_count} numeric strings.")

            cislo = [] # novy seznam, do ktereho budu pridavat promenne dle podminek nize
            for cisla in words_list:
                if cisla.isnumeric(): # vybiram pouze ciselne casti textu
                    cislo.append(cisla) # pridavam nalezene k seznamu cislo

            celkem_cisel = 0 # ciselna promenna yacinajici nulou, ke ktere pricitam dle podminek nize
            for n in cislo: # vychazim ze seznamu cislo
                celkem_cisel += int(n) # prevadim vse nalezene ze stringu na inegery a pricitam k ciselne promenne celkem_cisel

            print(f"The sum of all the numbers {celkem_cisel}.\n{line*40}")

            print("", "LEN", "|", "", "OCCURENCES ", "|", "NR.") # tady nevim, jak prizpusobit vysledny tisk tomu, jak je dlouhe odsazeni dle value
            print(line * 40)

            cetnost = [] # zakladam novy seznam
            for word in words_list: # vytvarim dilci promenne z celkoveho textu
                cetnost.append(len(word)) # ziskavam celkovou delku ziskaneho a pripojuji k seznamu cetnost

            frequency = dict() # novy slovnik
            for pocet_znaku in cetnost:
                frequency[pocet_znaku] = cetnost.count(pocet_znaku) # pridavam klic pocet_znaku a k nemu prirazuji soucet vseho v cetnosti

            for key, value in sorted(frequency.items()): # ctu z toho klice = pocty znaku, value = kolikrat se vyskztuji
                if key < 10: # podminka pro tisk jednocifernych poctu znaku, ciste kvuli hezcimu tisku
                    print("  ", key, "|", "*" * value, " " * (11 - value), "|", value)
                else:
                    print(" ", key, "|", "*" * value, " " * (11 - value), "|", value)

# DRUHA VOLBA UZIVATELE

        elif user_choice == "2":
            words_list = TEXTS[1].split()
            cista_slova = []
            for slovo in words_list:
                ciste = slovo.strip(".,")
                cista_slova.append(ciste)
            words_count = len(cista_slova)

            print(f"There are {str(words_count)} words in the selected text.") # tisk poctu slov

            title_count = 0
            for elem_title in words_list:
                if elem_title.istitle():
                    title_count += 1
                continue
            print(f"There are {title_count} titlecase words.")

            upper_count = 0
            for elem_upper in words_list:
                if elem_upper.isupper():
                    upper_count += 1
                continue
            print(f"There are {upper_count} uppercase words.")

            lower_count = 0
            for elem_lower in words_list:
                if elem_lower.islower():
                    lower_count += 1
                continue
            print(f"There are {lower_count} lowercase words.")

            numeric_count = 0 # celkovy pocet zacina na nule a nasledne se navysuje
            for elem_numeric in words_list: # nova promena vytvarena ze seznamu
                if elem_numeric.isnumeric(): # podminka pro vyber vsech slov s malym pismenem na zacatku
                    numeric_count += 1  # pricitam nalezena slova
                continue
            print(f"There are {numeric_count} numeric strings.")

            cislo = []
            for cisla in words_list:
                if cisla.isnumeric():
                    cislo.append(cisla)

            celkem_cisel = 0
            for n in cislo:
                celkem_cisel += int(n)
            print(f"The sum of all the numbers {celkem_cisel}.\n{line*40}")

            cetnost = []
            for word in words_list:
                cetnost.append(len(word))

            frequency = dict()
            for pocet_znaku in cetnost:
                frequency[pocet_znaku] = cetnost.count(pocet_znaku)

            print("", "LEN", "|", "  ", "OCCURENCES", "   ", "|", "NR.")
            print(line * 40)

            for key, value in sorted(frequency.items()):

                if key < 10:
                    print("  ", key, "|", "*" * value, " " * (16 - value), "|", value)
                else:
                    print(" ", key, "|", "*" * value, " " * (16 - value), "|", value)

# TRETI VOLBA UZIVATELE

        elif user_choice == "3":
            words_list = TEXTS[2].split()
            cista_slova = []
            for slovo in words_list:
                ciste = slovo.strip(".,")
                cista_slova.append(ciste)
            words_count = len(cista_slova)

            print(f"There are {str(words_count)} words in the selected text.") # tisk poctu slov

            title_count = 0
            for elem_title in words_list:
                if elem_title.istitle():
                    title_count += 1
                continue
            print(f"There are {title_count} titlecase words.")

            upper_count = 0
            for elem_upper in words_list:
                if elem_upper.isupper():
                    upper_count += 1
                continue

            print(f"There are {upper_count} uppercase words.")

            lower_count = 0
            for elem_lower in words_list:
                if elem_lower.islower():
                    lower_count += 1
                continue
            print(f"There are {lower_count} lowercase words.")

            numeric_count = 0
            for elem_numeric in words_list:
                if elem_numeric.isnumeric():
                    numeric_count += 1
                continue
            print(f"There are {numeric_count} numeric strings.")

            cislo = []
            for cisla in words_list:
                if cisla.isnumeric():
                    cislo.append(cisla)

            celkem_cisel = 0
            for n in cislo:
                celkem_cisel += int(n)
            print(f"The sum of all the numbers {celkem_cisel}.\n{line*40}")


            cetnost = []
            for word in words_list:
                cetnost.append(len(word))

            frequency = dict()
            for pocet_znaku in cetnost:
                frequency[pocet_znaku] = cetnost.count(pocet_znaku)

            print("", "LEN", "|", "  ", "OCCURENCES", "  ", "|", "NR.")
            print(line*40)

            for key, value in sorted(frequency.items()):
                if key < 10:
                    print("  ", key, "|", "*" * value, " " * (15 - value), "|", value)
                else:
                    print(" ", key, "|", "*" * value, " " * (15 - value), "|", value)
        else:
            print("Wrong choice!") # podminka pro pripad, zda ani jedna volba uzivatele nebude v rozmezi 1 - 3
            exit()

# zde se vracim k druhe podmince pro zadani hesla od uzavatele = pro pripad, kdy se heslo neschoduje s hodnotami ze slovniku users
    else:
        print("Spatne heslo")
    exit()

# 3. vytvarim podminku pro zjisteni platneho jmena uzivatele klice ze slovniku users:
else:
    print("Chybne uzivateslke jmeno")
    exit()