def isPrim(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def primekSzuper(szam):

    szuperPrimek = []
    sorszam = 0

    for i in range(2, szam + 1):
        if isPrim(i):
            sorszam = sorszam + 1
            if isPrim(sorszam):
                szuperPrimek.append(i)
    return szuperPrimek


kezdo = int(input("tól = "))
vege = int(input("ig = "))

lista = primekSzuper(vege)

print("Szuper primek a megadott tartományban:", [i for i in lista if i >= kezdo])