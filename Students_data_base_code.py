import random
import pandas as pd
import numpy as np

first_name_male = ["Jan", "Piotr", "Stanislaw", "Andrzej", "Pawel", "Jozef", "Krzysztof", "Adam", "Tomasz", "Marek",
                   "Michal",
                   "Jerzy", "Grzegorz", "Wojciech", "Marcin", "Kazimierz", "Tadeusz", "Lukasz", "Marian", "Antoni",
                   "Marian",
                   "Franciszek", "Zbigniew", "Jakub", "Robert", "Ryszard", "Mateusz", "Henryk", "Janusz", "Maciej",
                   "Karol",
                   "Mariusz", "Rafal", "Bogdan", "Rafal", "Roman", "Dariusz", "Aleksander", "Stefan", "Sebastian",
                   "Kamil",
                   "Edward", "Dawid", "Daniel", "Dominik", "Leszek", "Patryk", "Slawomir", "Szymon", "Sylwester",
                   "Waldemar",
                   "Kacper", "Arkadiusz", "Eugeniusz", "Ignacy", "Julian", "Leon", "Ludwik", "Witold", "Filip",
                   "Adrian",
                   "Cezary", "Feliks", "Hubert", "Lech", "Oskar", "Zenon", "Marcel", "Eryk", "Fabian", "Kajetan",
                   "Ksawery",
                   "Nikodem"]
first_name_female = ["Anna", "Maria", "Katarzyna", "Malgorzata", "Agnieszka", "Barbara", "Ewa", "Krystyna", "Magdalena",
                     "Krystyna", "Elzbieta", "Joanna", "Aleksandra", "Zofia", "Monika", "Teresa", "Danuta", "Natalia",
                     "Julia",
                     "Karolina", "Marta", "Beata", "Dorota", "Jadwiga", "Halina", "Janina", "Alicja", "Jolanta",
                     "Iwona", "Irena",
                     "Justyna", "Zuzanna", "Bozena", "Wiktoria", "Urszula", "Renata", "Hanna", "Sylwia", "Agata",
                     "Helena", "Maja",
                     "Patrycja", "Aneta", "Izabela", "Emilia", "Weronika", "Oliwia", "Ewelina", "Martyna", "Klaudia",
                     "Marianna",
                     "Marzena", "Gabriela", "Stanislawa", "Dominika", "Kinga", "Lena", "Edyta", "Amelia", "Kamila",
                     "Alina",
                     "Lidia", "Nikola", "Wioletta", "Kazimiera", "Laura", "Olga", "Jagoda"]

both_names = []
both_names.extend(first_name_male)
both_names.extend(first_name_female)
random.shuffle(both_names)

last_name_male = ["Nowak", "Kowalski", "Wisniewski", "Wajcik", "Kowalczyk", "Lewandowski", "Dabrowski", "Kozioł",
                  "Barczyk",
                  "Jasinski", "Baron", "Bielski", "Krawczyk", "Kwiatowski", "Mazur", "Kaczmarek", "Piotrowski",
                  "Grabowski",
                  "Janskowski", "Zajac", "Pawlowski", "Michalski", "Nowakowski", "Wiczorek", "Dudek", "Adamczyk",
                  "Nowicki",
                  "Olszewski", "Malinowski", "Jaworski", "Pawlak", "Witowski", "Sikora", "Walczak", "Rutkowski",
                  "Baran",
                  "Szewczyk", "Ostrowski", "Tomaszewski", "Zalewski", "Duda", "Marciniak", "Zawadzki", "Jakubowski",
                  "Wilk",
                  "Chmielewski", "Wlodarczyk", "Sawicki", "Lis", "Kucharski", "Mazurek", "Borowski", "Maciejowski",
                  "Wysocki",
                  "Kubiak", "Dubiel", "Kolodziejczyk", "Sobczak", "Konieczny", "Glowacki", "Krupa", "Wasilewski",
                  "Zakrzewski",
                  "Chabrzyk", "Sikorwski", "Laskowksi", "Gajewski", "Mostowiak", "Szulc", "Szymczak", "Kaszewski"]

last_name_female = ["Nowak", "Kowalska", "Wisniewska", "Wajcik", "Kowalczyk", "Lewandowska", "Dabrowska", "Zielinska",
                    "Szymanska", "Wolniak", "Janskowska", "Kwiatkowska", "Wojciechowska", "Krawczyk", "Kaczmarek",
                    "Piotrowska", "Grabowska", "Pawlowska", "Michalska", "Zajac", "Nowakowska", "Wieczorek", "Wrobel",
                    "Olszewska", "Adamczyk", "Dudek", "Malinowska", "Pawlak", "Witkowska", "Walczak", "Sikora",
                    "Rutkowska",
                    "Michalak", "Chabrzyk", "Baran", "Ostrowska", "Tomaszewska", "Szewczyk", "Zalewska", "Marciniak",
                    "Duda", "Sadowska", "Zawadzka", "Chmielewska", "Borkowska", "Wilk", "Jakubowska", "Lis",
                    "Maciejewska",
                    "Sawicka", "Kucharska", "Kalinowska", "Czarnecka", "Mazurek", "Wysocka", "Urbanska", "Kolodziej",
                    "Krajewska", "Zakrzewska", "Sikorska", "Adamska", "Sobczak", "Krupa", "Wasilewska", "Makowska",
                    "Szulc", "Gajewska", "Szymczak"]

wybor_studiów = ["Dzienne", "Zaoczne"]

semestr_nauczania = [1, 2]

kierunek_studiow_i_specjalizacja = {"Analityka Gospodarcza": ["Analityka Gospodarcza"],
                                    "Dziennikarstwo i komunikacja spoleczna": [
                                        "Nowe media i komunikacja elektroniczna w organizacjach",
                                        "Dziennikarstwo ekonomiczne i public relations",
                                        "Projektowanie komunikacji wizualnej i narracji"],
                                    "Ekonomia": ["Dystrybucja i sprzedaz na rynkach krajowych i miedzynarodowych",
                                                 "Ekonomia menadzerska",
                                                 "Gospodarska elektroniczna",
                                                 "Gospodarowanie nieruchomościami i usługi publiczne",
                                                 "Handel zagraniczny",
                                                 "International Commerce"],
                                    "Finanse Menadzerskie": ["Finanse Menadzerskie"],
                                    "Finance and Accountint for Business": ["Finance and Accountint for Business"],
                                    "Finanse i rachunkowosc": ["Analityk Finansowy",
                                                               "Finanse i technologie cyfrowe",
                                                               "Rachunkowosc i podatki",
                                                               "Rachunkowowsc i rewizja finansowa",
                                                               "Wspolczesna banskowosc"],
                                    "Finanse i rachunkowosc (Rybnik)": ["Analityk finansowy i rynkowy",
                                                                        "Rachunkowosc malych i srednich przedsiebiorstw"],
                                    "Finanse i zarzadznie w ochronie zdrowia": [
                                        "Finanse i zarzadznie w ochronie zdrowia"],
                                    "Gospodarka i zarzadzanie publiczne": ["Public relations w organizacjach",
                                                                          "Zarzadanie ryzykiem w organizacjach",
                                                                          "Zarzadzanie w organizacjach publicznych i spolecznych",
                                                                          "Zarzadzanie zasobami ludzkimi w administracji publicznej"],
                                    "Gospodarka cyfrowa": ["Gospodarka cyfrowa"],
                                    "Gospodarka miejska i nieruchomosci": ["Proramowanie rozwoju miast",
                                                                           "Nieruchomosci"],
                                    "Gospodarka przestrzenna": ["Gospodarka nieruchomosciami i planowanie przestrzenne",
                                                                "Analityka przestrzenna i srodowiskowa"],
                                    "Gospodarka turystyczna": ["Gospodarka turystyczna"],
                                    "Informatyka": ["Bazy danych i inżynieria danych",
                                                    "Programowanie gier i aplikacji mobilnych",
                                                    "Zintegrowane systemy informatyczne zarzadzania",
                                                    "Algorytmika i programowanie"],
                                    "Informatyka i Ekonometria": ["Analityk Danych",
                                                                  "Biznes elektroniczny",
                                                                  "Inzynieria wiedzy"],
                                    "International Business": ["International Business"],
                                    "Logistyka w biznesie": ["Obsluga logistyczna",
                                                             "Zaopatrzenie"],
                                    "Miedzynarodowe stosunki gospodarcze": ["Biznes miedzynarodowy",
                                                                            "Zarzadzanie miedzynarodowe"],
                                    "Przedsiebiorczosc i finanse": ["Przedsiebiorczosc i finanse"],
                                    "Zarzadzanie": ["Marketing",
                                                    "Zarzadzanie w uslugach",
                                                    "Zarzadzanie przedsiebiorstwem",
                                                    "Zarzadzanie zasobami ludzkimi"]}
#jakie_kierunek = random.choice(list(kierunek_studiow_i_specjalizacja.keys()))
# print(jakie_kierunek)
# print(random.choice(kierunek_studiow_i_specjalizacja[jakie_kierunek]))

oceny = [2, 2.5, 3, 3.5, 4, 4.5, 5]

wynik_rekturacji = [random.randint(42, 200) for i in range(0, len(first_name_female))]
# print(wynik_rekturacji)

miejsce_zamieszkania = ["Katowice", "Welnowiec", "Katowice Zawodzie", "Chorzow", "Bytkow", "Czeladz", "Sosnowiec",
                        "Zabrze",
                        "Gliwice", "Siemianowice Slaskie", "Kochlowice", "Ruda Slaska", "Wirek", "Tarnowskie Gory",
                        "Lagisza", "Dabrowa Gornicza", "Kazimierz Gorniczy", "Myslowice", "Jaworzno", "Tychy",
                        "Mikolow"]

max_liczba_studentow_na_specjalizacji = 30

aktualna_liczba_studentow_na_kierunku_x = [random.randint(30, 180) for i in range(0, 20)]
# print(aktualna_liczba_studentow_na_kierunku_x)

budynek_zajec = ["A", "B", "C", "E", "F", "L", "N", "CNTI", "Rybnik", "CINiBA"]
names = []
surnames = []
miejsce_zamieszkania_lista = []
rekturacja = []
wybor_studniow = []
semestr = []
kierunek = []
specjalizacja = []
srednia = []
opinia = []
students_dictionary = {}
for i in range(1, 4500+1):
    name = random.choice(both_names)
    if name in first_name_male:
        names.append(name)
        surnames.append(random.choice(last_name_male))
    else:
        names.append(name)
        surnames.append(random.choice(last_name_female))
    miejsce_zamieszkania_lista.append(random.choice(miejsce_zamieszkania))
    rekturacja.append(random.choice(wynik_rekturacji))
    wybor_studniow.append(random.choices(wybor_studiów,weights=[0.66, 0.33])[0])
    jaki_semestr = random.choice(semestr_nauczania)
    semestr.append(jaki_semestr)
    if jaki_semestr > 1:
        jaki_kierunek = random.choice(list(kierunek_studiow_i_specjalizacja.keys()))
        kierunek.append(jaki_kierunek)
        specjalizacja.append(random.choice(kierunek_studiow_i_specjalizacja[jaki_kierunek]))
        srednia.append(round(random.uniform(2.0, 5.0), 2))
        opinia.append(random.randint(1, 5))
    else:
        jaki_kierunek = random.choice(list(kierunek_studiow_i_specjalizacja.keys()))
        jaka_specjalizacja = None
        jaka_srednia = 0
        jaka_opinia = 0
        kierunek.append(jaki_kierunek)
        specjalizacja.append(jaka_specjalizacja)
        srednia.append(jaka_srednia)
        opinia.append(jaka_opinia)

students_dictionary["imie"] = names
students_dictionary["nazwisko"] = surnames
students_dictionary["miejsce_zamieszkania"] = miejsce_zamieszkania_lista
students_dictionary["wynik_rekturacji"] = rekturacja
students_dictionary["wybor_studiow"] = wybor_studniow
students_dictionary["semestr"] = semestr
students_dictionary["kierunek"] = kierunek
students_dictionary["specjalizacja"] = specjalizacja
students_dictionary["srednia_ocen"] = srednia
students_dictionary["opinia"] = opinia
#print(students_dictionary)

df = pd.DataFrame.from_dict(students_dictionary)
df.index = np.arange(1, len(df) + 1)
print(df.to_string())
df.to_csv("studenci2.csv", sep=',', encoding='utf-8')

#2/3 dzienne, 1/3 zaocznie


