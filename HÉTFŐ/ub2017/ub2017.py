class Eredmeny():
    def __init__(self, sor:str):
        adatok = sor.strip().split(";")
        self.nev = adatok[0]
        self.rajtszam = int(adatok[1])
        self.kategoria = adatok[2]
        temp = adatok[3].split(":")
        self.mp = int(temp[0]) * 3600 + int(temp[1]) * 60 + int(temp[2])
        self.versenyido = adatok[3]
        self.tavolsag = int(adatok[4])

file = open("ub2017egyeni.txt", "r", encoding="utf-8")
file.readline()

eredmenyek = []

for sor in file:
    eredmeny = Eredmeny(sor)
    eredmenyek.append(eredmeny)

file.close()

# 2. feladat

osszesen_versenyzok = 0

for eredmeny in eredmenyek:
    osszesen_versenyzok = osszesen_versenyzok + 1

print(f"3.2 feladat: Futók száma: {osszesen_versenyzok}")

# 3. feladat

noi_sportolok = 0

for eredmeny in eredmenyek:
    if eredmeny.kategoria == "Noi" and eredmeny.tavolsag == 100:
        noi_sportolok = noi_sportolok + 1


print(f"3.3 feladat: Célba érkező női sportolók: {noi_sportolok} fő")

# 4. feladat

legh_nev = eredmenyek[0]

for eredmeny in eredmenyek:
    if len(eredmeny.nev) > len(legh_nev.nev):
        legh_nev = eredmeny

print(f"3.4 feladat: A leghosszabb nevű futó\n\tNév:{legh_nev.nev}\n\tRajtszám: {legh_nev.rajtszam}\n\tEredmeny: {legh_nev.versenyido}")


# 5. feladat


osszes_ffi = 0
osszes_mp = 0

for eredmeny in eredmenyek:
    if eredmeny.kategoria == "Ferfi" and eredmeny.tavolsag == 100:
        osszes_ffi = osszes_ffi + 1
        osszes_mp = osszes_mp + eredmeny.mp

atlag = ( osszes_mp / osszes_ffi ) / 3600

print(f"3.5 Férfi sportólok átlagos ideje: {atlag} óra ")

