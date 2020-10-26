# PYTANIE NR 1 Ile kontenerów finalnie trafi do Japonii (JP)? (liczba kontenerów) – 15 pkt

with open('dane.csv', 'r') as csvfile:
    mylist = csvfile.readlines()
    res = [sub[:-1] for sub in mylist[1:]]
    bez_srednika = []
    licznikKrajow = 0
    for line in res:
        new_line = line.split(';')
        bez_srednika.append(new_line)
    for line in bez_srednika:
        for item in line:
            if item == '':
                continue
            kraj_pochodzenia = item[0:2]
            kraj_docelowy = item[3:5]
            numer_kontenera = item[6:14]
            waga = float(item[15:19])
            typ_ladunku = item[20:22]
            reszta = item[23:]
            firma, cena = reszta.split('/')
            cena = int(cena)
            nazwa_firmy = firma[:-3]
            kraj_firmy = firma[-2:]

            stosunek = float(cena / waga)

            if kraj_docelowy == 'JP':
                licznikKrajow += 1

print(licznikKrajow)

# PYTANIE NR. 2 Jaka klasa statku średnio przewozi najwięcej kontenerów? (sama nazwa klasy statku) – 15 pkt


with open('dane.csv', 'r') as csvfile:
    mylist = csvfile.readlines()
    dictionary = {}
    ships = mylist[0]
    ships = ships.split(";")
    for ship in ships:
        dictionary[ship] = 0

    res = [sub[:-1] for sub in mylist]
    bez_srednika = []
    for line in res:
        new_line = line.split(';')
        bez_srednika.append(new_line)
    waga = 0.0
    ilosc_kontenerow = 0
    for line in bez_srednika:
        for index, item in enumerate(line):
            if len(item) > 0:
                dictionary[ships[index]] += 1

print(dictionary)

occurrences = 0
containers = 0
for item in dictionary:
    if item.find("ULCV") > 0:
        occurrences += 1
        containers += dictionary[item]

print(containers / occurrences)



# PYTANIE NR. 3 Jaka jest średnia waga kontenera z przetworami owocowymi (A3) z dokładnością do 1 kg np: 1234? (zaokrąglane w górę) – 20 pkt


with open('dane.csv', 'r') as csvfile:
    mylist = csvfile.readlines()
    res = [sub[:-1] for sub in mylist]
    bez_srednika = []
    for line in res:
        new_line = line.split(';')
        bez_srednika.append(new_line)
    waga = 0.0
    ilosc_kontenerow = 0
    for line in bez_srednika:
        for item in line:
            if "/A3@" in item:
                waga += float(item[15:19])
                ilosc_kontenerow += 1
print(waga / ilosc_kontenerow)

# PYTANIE NR. 4 Która Polska firma globalnie przewozi najwięcej kontenerów? (nazwa firmy) – 25 pkt


with open('dane.csv', 'r') as csvfile:  # otwieram CSV
    mylist = csvfile.readlines()  # robie readlines i przypisuje do zmiennej mylist
    res = [sub[:-1] for sub in mylist]  # ucinam ostatni znak
    bez_srednika = []  # tworze nowa liste, na razie pusta do ktorej wloze linijki po splitowaniu o ";"
    for line in res:  # iteruje po linijkach listy res
        new_line = line.split(';')  # stworzylem new_line, ktory jest elementem do appendowania do nowej listy
        bez_srednika.append(new_line)  # dodaje do nowej listy kazdy zmieniony element
    waga = 0.0
    ilosc_kontenerow = 0
    slownik_nazw_firmy = {}
    for line in bez_srednika:
        for item in line:
            if ".pl" in item:
                nazwa_firmy = item[item.find('@') + 1:item.find('.')]
                value = 1
                if nazwa_firmy not in slownik_nazw_firmy:
                    slownik_nazw_firmy[nazwa_firmy] = 1
                else:
                    slownik_nazw_firmy[nazwa_firmy] = slownik_nazw_firmy[nazwa_firmy] + 1

ilosc_kontenerow_max = 0
nazwa_firmy_max = ""
for nazwa_firmy, ilosc_kontenerow in slownik_nazw_firmy.items():
    if ilosc_kontenerow > ilosc_kontenerow_max:
        ilosc_kontenerow_max = ilosc_kontenerow
        nazwa_firmy_max = nazwa_firmy

print(nazwa_firmy_max, ilosc_kontenerow_max)
print(slownik_nazw_firmy)

# PYTANIE NR. 5 Jakiego typu ładunek o największej wartości eksportują Niemieckie firmy z Niemiec? (wartość to stosunek ceny do wagi) – 25 pkt


with open('dane.csv', 'r') as csvfile:
    mylist = csvfile.readlines()
    res = [sub[:-1] for sub in mylist[1:]]
    bez_srednika = []
    dictionary_stosunkow = {}
    for line in res:
        new_line = line.split(';')
        bez_srednika.append(new_line)
    for line in bez_srednika:
        for item in line:
            if item == '':
                continue
            kraj_pochodzenia = item[0:2]
            kraj_docelowy = item[3:5]
            numer_kontenera = item[6:14]
            waga = float(item[15:19])
            typ_ladunku = item[20:22]
            reszta = item[23:]
            firma, cena = reszta.split('/')
            cena = int(cena)
            nazwa_firmy = firma[:-3]
            kraj_firmy = firma[-2:]

            stosunek = float(cena / waga)

            if kraj_firmy == 'de' and kraj_pochodzenia == 'DE':
                dictionary_stosunkow[typ_ladunku] = stosunek

print(dictionary_stosunkow)
