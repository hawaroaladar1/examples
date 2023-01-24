class Beosztas():
    def __init__(self, nev:str, tantargy:str, osztaly:str, heti_oraszam:str):
        self.nev = nev.strip()
        self.tantargy = tantargy.strip()
        self.osztaly = osztaly.strip()
        self.heti_oraszam = int(heti_oraszam.strip())

file = open("beosztas.txt", "r", encoding="utf-8")

sorok = file.readlines()
bejegy_osszesen = int(len(sorok) / 4)

beosztasok = []

for i in range(bejegy_osszesen):
    
    nev = sorok[i * 4]
    tantargy = sorok[i * 4 + 1]
    osztaly = sorok[i * 4 + 2]
    heti_oraszam = sorok[i * 4 + 3]

    beosztas = Beosztas(nev, tantargy, osztaly, heti_oraszam)
    beosztasok.append(beosztas)

file.close()

# 2. feladat

bejegy_db = 0

for beosztas in beosztasok:
    bejegy_db = bejegy_db + 1

print(f"2. feladat\nA fájlban {bejegy_db} bejegyzés van")

# 3. feladat

osszes_tanora = 0

for beosztas in beosztasok:
    osszes_tanora = osszes_tanora + beosztas.heti_oraszam

print(f"3. feladat\nAz iskolában a heti összóraszám: {osszes_tanora}")

# 4. feladat

tanar_nev = input("Egy tanár neve = ")
tanar_oraja = 0

for beosztas in beosztasok:
    if tanar_nev == beosztas.nev:
        tanar_oraja = tanar_oraja + beosztas.heti_oraszam

print(f"3. feladat\nA tanár heti óraszáma: {tanar_oraja}")

# 5. feladat

file01 = open("of.txt" ,"w" , encoding="utf-8")

for beosztas in beosztasok:
    if beosztas.tantargy == "osztalyfonoki":
        file01.write(f"{beosztas.osztaly} - {beosztas.nev}\n")

file01.close()

# 6. feladat

print("6. feladat")
osztaly_be = input("Osztály = ") 
tantargy_be = input("Tantárgy = ")

szamlalo = 0

for beosztas in beosztasok:
    if beosztas.osztaly == osztaly_be and beosztas.tantargy == tantargy_be:
        szamlalo = szamlalo + 1

if szamlalo > 1:
    print("Csoportbontásban tanulják! ")
else:
    print("Osztályszinten tanulják! ")


# 7. feladat

tanarok_osszesen = []

for beosztas in beosztasok:
    if beosztas.nev not in tanarok_osszesen:
        tanarok_osszesen.append(beosztas.nev)

print(f"Az iskolában {len(tanarok_osszesen)} tanár tanít")