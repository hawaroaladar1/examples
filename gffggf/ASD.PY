def isPrim(szam):
    if szam < 2:
        return False
    for i in range(2, szam):
        if szam % i == 0:
            return False

    return True


def szuperPrim(num):

    szuperPrimLista = []
    sorszam = 0

    for i in range(2, num + 1):
        if isPrim(i):
            sorszam = sorszam + 1
            if isPrim(sorszam):
                szuperPrimLista.append(i) 

    return szuperPrimLista   


kezdo = int(input("Kezdo: "))
vege = int(input("Vege: "))

listacskam = szuperPrim(vege)

print(f"Szuperek: ", [i for i in listacskam if i >= kezdo])