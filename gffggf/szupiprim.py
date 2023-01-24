def isPrim(szam):
    if szam < 2:
        return False
    for i in range(2, szam):
        if szam % i == 0:
            return False
        
    return True

def szuperPrimek(num):

    primekSzuper = []
    sorszam = 0

    for i in range(2, num + 1):
        if isPrim(i):
            sorszam = sorszam + 1
            if isPrim(sorszam):
                primekSzuper.append(i)
    return primekSzuper


kezdo = int(input("Adjon meg egy kezdőt! "))
vege = int(input("Adja meg a végét! "))

listacskam = szuperPrimek(vege)

print(f"Szuper primek: ", [ i for i in listacskam if i >= kezdo])